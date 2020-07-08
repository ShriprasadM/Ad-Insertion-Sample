import requests
from ctypes import *
import os
import xml.etree.ElementTree as ET
import json
import urllib
#import vastgen.vast as vst
import sys
import html
import sample

def injestOWBidsInGADServer(minDuration, maxDuration, owr) :

    customParams = """
        &pwtbst={pwtbst}
        &pwtbst_pubmatic={pwtbst_pubmatic}
        &pwtcid={pwtcid}
        &pwtcid_pubmatic={pwtcid_pubmatic}
        &pwtcpath={pwtcpath}
        &pwtcurl={pwtcurl}
        &pwtdid={pwtdid}
        &pwtdid_pubmatic={pwtdid_pubmatic}
        &pwtdur={pwtdur}
        &pwtecp={pwtecp}
        &pwtecp_pubmatic={pwtecp_pubmatic}
        &pwtpid={pwtpid}
        &pwtpid_pubmatic{pwtpid_pubmatic}
        &pwtplt={pwtplt}
        &pwtprofid={pwtprofid}
        &pwtpubid={pwtpubid}
        &pwtsid={pwtsid}
        &pwtsid_pubmatic={pwtsid_pubmatic}
        &pwtsz={pwtsz}
        &pwtsz_pubmatic={pwtsz_pubmatic}
        &pwtverid={pwtverid}
    """.format(
        pwtbst =owr["pwtbst"], 
        pwtbst_pubmatic =owr["pwtbst_pubmatic"],
        pwtcid =owr["pwtcid"],
        pwtcid_pubmatic =owr["pwtcid_pubmatic"], 
        pwtcpath =owr["pwtcpath"],
        pwtcurl =owr["pwtcurl"],
        pwtdid =owr["pwtdid"],
        pwtdid_pubmatic =owr["pwtdid_pubmatic"],
        pwtdur =owr["pwtdur"],
        pwtecp =owr["pwtecp"],
        pwtecp_pubmatic =owr["pwtecp_pubmatic"],
        pwtpid =owr["pwtpid"],
        pwtpid_pubmatic =owr["pwtpid_pubmatic"],
        pwtplt =owr["pwtplt"],
        pwtprofid =owr["pwtprofid"],
        pwtpubid =owr["pwtpubid"],
        pwtsid =owr["pwtsid"],
        pwtsid_pubmatic =owr["pwtsid_pubmatic"],
        pwtsz =owr["pwtsz"],
        pwtsz_pubmatic =owr["pwtsz_pubmatic"],
        pwtverid =owr["pwtverid"]
        )
    params = urllib.parse.quote("".join(customParams.split()))

    #print("Params = " , params)


    adRequest = """ 
    https://pubads.g.doubleclick.net/gampad/ads?iu=/15671365/SM_HK_20_AU
    &description_url=http://google.com
    &tfcd=0
    &npa=0
    &sz=320x254
    &cust_params={params}
    &min_ad_duration={minDuration}
        &max_ad_duration={maxDuration}
        &gdfp_req=1
        &output=vast
        &unviewed_position_start=1
        &env=vp
        &correlator=[placeholder]
        &vpmute=0
        &vpa=0
        &url=http://google.com&vpos=preroll
    """.format(params = params, minDuration = minDuration, maxDuration = maxDuration)

    call = "".join(adRequest.split())
    #print(call)
    return call


def callGuaranteedAdServer(msg, db, jsonResponse):
    # duration = msg.time_range[1]-msg.time_range[0]
    # print("query db with time range: "+str(msg.time_range[0])+"-"+str(msg.time_range[1]))
    # metaData = db.query(msg.content, msg.time_range, msg.time_field)
    adMinDuration = 5000 # 5 sec
    adMaxDuration = 17000 # 15 sec

   

    try:

        #owr = json.loads(sample.ow_dummy_respose.replace("'","\""))
        print("Preparing GAM call by injecting OW values")
      #  owr = json.loads(jsonResponse.replace("'","\""))
          owr = sample.ow_dummy_respose
       # owr = jsonResponse
        callCnt = 1
        bidResponses = []
        for impid in owr :
            print(impid)
            for bid in owr[impid] :
                #print(bid)
                gam = injestOWBidsInGADServer(adMinDuration,adMaxDuration, bid)
                r = requests.get(gam)
                vast = r.text
                callCnt += 1
                # TODO call unwrap VAST End point
                if vast == None :
                    print("GAM Call ", str(callCnt), "Error :: GAM return empty VAST")
                else :
                    print("SHRI :: success GAM")
                    print("GAM Call ", str(callCnt), " Response = ", vast)

                    #TDOO unwrap call
                    print("Getting Media File from VAST")
                    vastNodes = ET.fromstring(vast)
                    for node in vastNodes.iter():
                        if node.tag == "MediaFile":
                            bidResponses.append(node.text)
                            break
                


        print("all Media Files are collected = ", bidResponses)
        return bidResponses
        
        
    except Exception as e:
        print("Error in calling GAM")
        print(e)
        # print(traceback.format_exc(), flush=True)
        return None



# def vastBuilder() :
#     print ("builder")


#     vast = vst.VAST({"version":"3.0", "VASTErrorURI": "optional url if something went wrong in client side"})
#     ad = vast.attachAd({ 
#         "id": "1", # ad id 
#         "structure": 'inline', # or "wrapper", 
#         "sequence": "1", # optional, not required
#         "Error": 'http://error.err', # error url if something went wrong in client side, optional
#         "AdTitle": 'Common name of the ad' , # required for inline structure, 
#         "AdSystem": { "name": 'name of adserver or company', "version": "1.0"  }, 
#         "Description": "optional description of ad",
#         "Advertiser": "Optional name of advertiser",
#         "Pricing": "Optional price (if you want to RTB on vast)",
#         "Extensions": "",
#         })
    
#     ad.attachImpression({
#           "id": "adstitcher",
#          "url": "http://adstitcher.com"
#     })
#     ur = json.loads(sample.example2)  
#     creatives = ur["ads"][0]["creatives"]
#     for cr in creatives:
#         if  not "mediaFiles" in cr:
#             continue
        
#         creative = ad.attachCreative('Linear', {
#                     "Duration" : '00:00:30'
#                 })
#         if  "mediaFiles" in cr:
#             for med in cr["mediaFiles"]:
                
#                 creative.attachMediaFile(med["fileURL"],{
#                     "id" : med["id"],
#                     "type" : med["mimeType"],
#                     "bitrate" : str(med["bitrate"]),
#                     "minBitrate": str(med["minBitrate"]), 
#                     "maxBitrate": str(med["maxBitrate"]),
#                     "width" : str(med["width"]),
#                     "height" : str(med["height"]),
#                     "maintainAspectRatio" : "true",
#                     "codec" : med["codec"],
#                 })

#         if "videoClickTrackingURLTemplates" in cr:
#             for url in cr["videoClickTrackingURLTemplates"]:
#                 # attach video click tracking event
#                 creative.attachVideoClick('ClickThrough', url)
        
    
  
   
#     v = vast.xml()
    
#     mergedXml = html.unescape(" ".join(str(v).split()).replace("\\n"," ").replace("'","".replace("\b","")))
#     mergedXml = mergedXml.replace("b<VAST>", "<VAST version=\"3.0\">")
#     print(mergedXml)





  

def testWithOw() :
 
    # url = 'http://172.16.4.192:9009/video/json'
    # params = {
    #     "app.name": "OpenWrapperSample",
    #     "app.ver": 1.0,
    #     "app.storeurl": "https%3A%2F%2Fitunes.apple.com%2Fus%2Fapp%2Fpubmatic-sdk-app%2Fid1175273098%3Fvideobid%3D10%26advdomainres%3D1%26vidimprand%3D1",
    #     "app.pub.id": 5890,
    #     "app.bundle": "com.pubmatic.openbid.app",
    #     "req.id": "1559039248176",
    #     "imp.id": "28635736ddc2bb1",
    #     "imp.tagid": "/15671365/MG_VideoAdUnit",
    #     "imp.vid.mimes": "video%2F3gpp%2Cvideo%2Fmp4%2Cvideo%2Fwebm",
    #     "imp.vid.minduration": 30,
    #     "imp.vid.maxduration": 90,
    #     "imp.vid.ext.adpod.adminduration": 20,
    #     "imp.vid.ext.adpod.admaxduration": 30,
    #     "imp.vid.ext.adpod.minads": 2,
    #     "imp.vid.ext.adpod.maxads": 4,
    #     "imp.vid.ext.adpod.excliabcat": 100,
    #     "imp.vid.ext.adpod.excladv": 100,
    #     "req.ext.wrapper.versionid": 1,
    #     "req.ext.wrapper.ssauction": 0,
    #     "req.ext.wrapper.sumry_disable": 0,
    #     "req.ext.wrapper.clientconfig": 1,
    #     "req.ext.wrapper.profileid": 2953
    # }
    # response = requests.get(url, params)

    # response.raise_for_status()
    # # access JSOn content
    # jsonResponse = response.json()
    jsonResponse = sample.ow_dummy_respose
    #print("JSON response from " + url + " :")
    print(jsonResponse)
    return jsonResponse


#if __name__ == "__main__":
      #  owResponse = testWithOw()
       # callGuaranteedAdServer(None, None, owResponse)
#        vastBuilder()


    # path = os.getcwd() + "/ad-insertion/ad-transcode/golib"
    #        class go_string(Structure):
    #         _fields_ = [
    #         ("p", c_char_p),
    #         ("n", c_int)
    #         ]

    #     lib = CDLL(path + "/unwrapvast.dylib")
    #     str1 = c_char_p( "vast")
    #     b = go_string(str1, len(str1))
    #     lib.bar.restype = c_char_p
    #     a = lib.UnwrapVast(b)
    #     print (a)    