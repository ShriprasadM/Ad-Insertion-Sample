import requests
from ctypes import *
import os
import xml.etree.ElementTree as ET
import json
import urllib
unwrapperUrl = "http://localhost:3000/api/unwrapVast"
sampleOWResponse = """
{
  "28635736ddc2bb1": [{
    "pwtbst": "1",
    "pwtbst_pubmatic": "1",
    "pwtcid": "2befe49a-63d3-4da0-a512-a1ee5df86382",
    "pwtcid_pubmatic": "2befe49a-63d3-4da0-a512-a1ee5df86382",
    "pwtcpath": "/cache",
    "pwtcurl": "http://172.16.4.192:2424",
    "pwtdid": "PUBDEAL1",
    "pwtdid_pubmatic": "PUBDEAL1",
    "pwtdur": "25",
    "pwtecp": "9.00",
    "pwtecp_pubmatic": "9.00",
    "pwtpid": "pubmatic",
    "pwtpid_pubmatic": "pubmatic",
    "pwtplt": "video",
    "pwtprofid": "2953",
    "pwtpubid": "5890",
    "pwtsid": "/15671365/MG_VideoAdUnit",
    "pwtsid_pubmatic": "/15671365/MG_VideoAdUnit",
    "pwtsz": "0x0",
    "pwtsz_pubmatic": "0x0",
    "pwtverid": "1"
  }, {
    "pwtbst": "1",
    "pwtbst_pubmatic": "1",
    "pwtcid": "73e29c4e-d70e-44dc-b64c-80cf9edf6a29",
    "pwtcid_pubmatic": "73e29c4e-d70e-44dc-b64c-80cf9edf6a29",
    "pwtcpath": "/cache",
    "pwtcurl": "//172.16.4.192:2424",
    "pwtdid": "PUBDEAL1",
    "pwtdid_pubmatic": "PUBDEAL1",
    "pwtdur": "25",
    "pwtecp": "9.00",
    "pwtecp_pubmatic": "9.00",
    "pwtpid": "pubmatic",
    "pwtpid_pubmatic": "pubmatic",
    "pwtplt": "video",
    "pwtprofid": "2953",
    "pwtpubid": "5890",
    "pwtsid": "/15671365/MG_VideoAdUnit",
    "pwtsid_pubmatic": "/15671365/MG_VideoAdUnit",
    "pwtsz": "0x0",
    "pwtsz_pubmatic": "0x0",
    "pwtverid": "1"
  }, {
    "pwtbst": "1",
    "pwtbst_pubmatic": "1",
    "pwtcid": "548da009-1f7b-44dc-876a-10f6b90a7473",
    "pwtcid_pubmatic": "548da009-1f7b-44dc-876a-10f6b90a7473",
    "pwtcpath": "/cache",
    "pwtcurl": "//172.16.4.192:2424",
    "pwtdid": "PUBDEAL1",
    "pwtdid_pubmatic": "PUBDEAL1",
    "pwtdur": "20",
    "pwtecp": "9.00",
    "pwtecp_pubmatic": "9.00",
    "pwtpid": "pubmatic",
    "pwtpid_pubmatic": "pubmatic",
    "pwtplt": "video",
    "pwtprofid": "2953",
    "pwtpubid": "5890",
    "pwtsid": "/15671365/MG_VideoAdUnit",
    "pwtsid_pubmatic": "/15671365/MG_VideoAdUnit",
    "pwtsz": "0x0",
    "pwtsz_pubmatic": "0x0",
    "pwtverid": "1"
  }, {
    "pwtbst": "1",
    "pwtbst_pubmatic": "1",
    "pwtcid": "fa2336d6-4196-4c90-ba71-519d2be1ef21",
    "pwtcid_pubmatic": "fa2336d6-4196-4c90-ba71-519d2be1ef21",
    "pwtcpath": "/cache",
    "pwtcurl": "//172.16.4.192:2424",
    "pwtdid": "PUBDEAL1",
    "pwtdid_pubmatic": "PUBDEAL1",
    "pwtdur": "20",
    "pwtecp": "9.00",
    "pwtecp_pubmatic": "9.00",
    "pwtpid": "pubmatic",
    "pwtpid_pubmatic": "pubmatic",
    "pwtplt": "video",
    "pwtprofid": "2953",
    "pwtpubid": "5890",
    "pwtsid": "/15671365/MG_VideoAdUnit",
    "pwtsid_pubmatic": "/15671365/MG_VideoAdUnit",
    "pwtsz": "0x0",
    "pwtsz_pubmatic": "0x0",
    "pwtverid": "1"
  }]
}
"""

def getParsedVast(vastXmlURl, pwturl):
    try:
        myobject = {
            "adm":vastXmlURl
        }
        unwrappedvast = requests.post(unwrapperUrl, json=myobject).json()
        
        if len(unwrappedvast['ads']) == 0:
            myobject.adm = pwturl
            unwrappedvast = requests.post(unwrapperUrl, json=myobject)
        return unwrappedvast
    except Exception as e:
        print("Error in calling unwrapper")
        print(e)
        # print(traceback.format_exc(), flush=True)
        return None 

def getMediaFile(parsedVast):
    try:
        newMediaObjects =[]
        ads = parsedVast['ads']
        for ad in ads:
            creatives = ad['creatives']
            for creative in creatives:
                isVideoCreative = False
                mediaObject = {}
                if len(creative['mediaFiles']) > 0:
                    mediaFiles = creative['mediaFiles']
                    for mediaFile in mediaFiles:
                        if 'mimeType' in mediaFile: 
                            isVideoCreative= True
                            mediaObject['mediaFile'] = mediaFile
                    if isVideoCreative == True:
                        mediaObject['trackingEvents'] = creative['trackingEvents']
                isEmpty = not bool(mediaObject)
                if isEmpty == False:
                    newMediaObjects.append(mediaObject)
        return newMediaObjects
    except Exception as e:
        print("Error in getting Media File", e)
        return None

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

def callGuaranteedAdServer(msg, db, jsonResponse, isSSAI):
    # duration = msg.time_range[1]-msg.time_range[0]
    # print("query db with time range: "+str(msg.time_range[0])+"-"+str(msg.time_range[1]))
    # metaData = db.query(msg.content, msg.time_range, msg.time_field)
    adMinDuration = 5000 # 5 sec
    adMaxDuration = 17000 # 15 sec

   

    try:

        owr = json.loads(sampleOWResponse.replace("'","\""))

        callCnt = 1
        bidResponses = []
        mediaObjects = []
        for impid in owr :
            print(impid)
            for bid in owr[impid] :
                #print(bid)
                gam = injestOWBidsInGADServer(adMinDuration,adMaxDuration, bid)
                # r = requests.get(gam)
                pwturl = bid['pwtcurl'] + bid['pwtcpath'] + '/?uuid=' + bid['pwtcid']
                vast = getParsedVast(gam, pwturl) #pwturl= xml hosted url ow.pubmatic.com/cacheid=cacheid
                # vast = r.text
                if vast and len(vast['ads']) > 0:
                    bidResponses.append(vast['ads'])
                callCnt += 1
                # TODO call unwrap VAST End point
                #TODO RETURN MEDIA FILES, Tracking Events and click Events
                if isSSAI == True:
                    mediaObjects.append(getMediaFile(vast))
                #Baed on flag
                # if vast == None :
                #     print("GAM Call ", str(callCnt), "Error :: GAM return empty VAST")
                # else :
                #     print("SHRI :: success GAM")
                #     print("GAM Call ", str(callCnt), " Response = ", vast)

                #     #TDOO unwrap call
                #     print("Getting Media File from VAST")
                #     vastNodes = ET.fromstring(vast)
                #     for node in vastNodes.iter():
                #         if node.tag == "MediaFile":
                #             bidResponses.append(node.text)
                #             break
                # bidResponses.append(vast)
                

        print("all Media Files are collected = ", bidResponses)
        return bidResponses
        
        
    except Exception as e:
        print("Error in calling GAM")
        print(e)
        # print(traceback.format_exc(), flush=True)
        return None

if __name__ == "__main__":
    callGuaranteedAdServer(None, None, None,True)



    # path = os.getcwd() + "/ad-insertion/ad-transcode/golib"
    #     class go_string(Structure):
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