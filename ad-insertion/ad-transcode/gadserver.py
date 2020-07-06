import requests
from ctypes import *
import os
import xml.etree.ElementTree as ET

def callGuaranteedAdServer(msg, db):
    # duration = msg.time_range[1]-msg.time_range[0]
    # print("query db with time range: "+str(msg.time_range[0])+"-"+str(msg.time_range[1]))
    # metaData = db.query(msg.content, msg.time_range, msg.time_field)
    gam = "https://pubads.g.doubleclick.net/gampad/ads?iu=/15671365/SM_HK_20_AU&description_url=http%3A%2F%2Fgoogle.com&tfcd=0&npa=0&sz=320x254&min_ad_duration=15000&max_ad_duration=17000&gdfp_req=1&output=vast&unviewed_position_start=1&env=vp&correlator=[placeholder]&vpmute=0&vpa=0&url=http%3A%2F%2Fgoogle.com&vpos=preroll"
    try:
        r = requests.get(gam)


        #print(r.text)

        r1 = """<?xml version="1.0" encoding="UTF-8"?>
            <VAST xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="vast.xsd" version="3.0">
            <Ad id="5413948756">
            <InLine>
            <AdSystem>GDFP</AdSystem>
            <AdTitle>SM_HK_20_VID_15_Sec</AdTitle>
            <Description><![CDATA[SM_HK_20_VID_15_Sec ad]]></Description>
            <Error><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=videoplayfailed[ERRORCODE]]]></Error>
            <Impression><![CDATA[https://securepubads.g.doubleclick.net/pcs/view?xai=AKAOjsvPJjw0c3uWZ1gx5dKuYVm2AzusjlTSy8X8nU59XxmJs-b1siuCpZJnUsfDxmIPz88I1Yyf7zqSRgZK9jrajErDfAq4E8GCvYIy9Nmn6oSmxIh42WdcEpMlIrZe9QrV0-gmW6R2Y6P25gu6HGuwDtANjsADO3qN0K58DaB_v2rUHmD5ZP6V0t3AobGCSye-G60EcsRHPUxouGFSE-ANyfqpeEIYE9S9gTIxBGRLHuRZqQo2kbGCUgdJoFE0ROFlcpKKd52FwJfQFOM&sig=Cg0ArKJSzCutO9m7OWM4EAE&adurl=]]></Impression>
            <Creatives>
                <Creative id="138316111139" sequence="1">
                <Linear>
                <Duration>00:00:15</Duration>
                <TrackingEvents>
                <Tracking event="start"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=part2viewed&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="firstQuartile"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=videoplaytime25&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="midpoint"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=videoplaytime50&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="thirdQuartile"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=videoplaytime75&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="complete"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=videoplaytime100&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="mute"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=admute&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="unmute"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=adunmute&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="rewind"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=adrewind&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="pause"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=adpause&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="resume"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=adresume&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="creativeView"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=vast_creativeview&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="fullscreen"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=adfullscreen&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="acceptInvitationLinear"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=acceptinvitation&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="closeLinear"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=adclose&ad_mt=[AD_MT]]]></Tracking>
                <Tracking event="exitFullscreen"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=vast_exit_fullscreen&ad_mt=[AD_MT]]]></Tracking>
                </TrackingEvents>
                <VideoClicks>
                <ClickThrough id="GDFP"><![CDATA[https://pubads.g.doubleclick.net/pcs/click?xai=AKAOjsur0mPtRH1jDGyA7WIu4_SjQBof4eBQVsZnVMTqZi7-LMnJ8cAGtUxVLKxpTW35XVYEccRntHbKcL6Q8km-2fSFrHAvuQQTHPCsLBTA4xLzo0PFZOOyD0sH6nsCfDNj-k_nyHD6w2KGzr8IGpyux61puf3LRUuiFcKtMS6QDmEDEd9yGYR3l9hh2B8R_pc4PpyFVf8q3t1UHSml7W7X6V3QVNkEv_Tp9n7YbJw3FeQLsaU4YpuoH9KGgcNVTpm7rsgJq-a3nHk&sig=Cg0ArKJSzCA-u59gDrrg&adurl=http://test.com]]></ClickThrough>
                </VideoClicks>
                <MediaFiles>
                <MediaFile id="GDFP" delivery="progressive" width="1280" height="720" type="video/mp4" bitrate="1033" scalable="true" maintainAspectRatio="true"><![CDATA[https://iab-publicfiles.s3.amazonaws.com/vast/VAST-4.0-Short-Intro.mp4]]></MediaFile>
                </MediaFiles>
                </Linear>
                </Creative>
            </Creatives>
            <Extensions><Extension type="geo"><Country>IN</Country><Bandwidth>4</Bandwidth><BandwidthKbps>16240</BandwidthKbps></Extension><Extension type="metrics"><FeEventId>sPABX8u2IMSmwgPW1YroCA</FeEventId><AdEventId>CIa4h9e1tuoCFVAljwodqmcO1Q</AdEventId></Extension><Extension type="ShowAdTracking"><CustomTracking><Tracking event="show_ad"><![CDATA[https://securepubads.g.doubleclick.net/pcs/view?xai=AKAOjsuIEPl7_1CALeFeLKF3qNgZYjyUok_C8Qj-m4XjWhLsd8f2Cf3G8yBVzagTekevoIRu-qjF3cs1jjwE09Lp1DH6KNTC0tuLhT2UQNBWgO_wzgucM8axKlyB_K7XOSKaEUCTLZ9YO1DGPxtKMj0YTP4iKlO9HTO2aCm30qNYn3dKRlEiUEIzcSMfd8PGgZppvFTLaovUBJqQDlQFEcqmYndAT-j6UEEAZDjQcj5m1HUjT_eATdKeUxY8lBAXbWQ73zSVHnW6rkvx-62b2w&sig=Cg0ArKJSzD-QlzLacBoHEAE&adurl=]]></Tracking></CustomTracking></Extension><Extension type="video_ad_loaded"><CustomTracking><Tracking event="loaded"><![CDATA[https://pubads.g.doubleclick.net/pagead/conversion/?ai=BOWldsPABX4agIdDKvASqz7moDfb6_eFFAAAAEAEg0fv0CDgAWKO6oaKDBGDl6uaDvA6yAQpnb29nbGUuY29tugETMzAweDIzOSwzMjB4MjU0X3htbMgBBdoBEmh0dHA6Ly9nb29nbGUuY29tL5gCCsACAuACAOoCFS8xNTY3MTM2NS9TTV9IS18yMF9BVfgChNIekAOaCJgD4AOoAwHgBAHSBQYQ1JrJlRSQBgGgBiOoB-zVG6gH89EbqAeW2BuoB8LaG9gHAeAHH9IIBwiAYRABGB2YCwE&sigh=3-gGymBUsL8&label=video_ad_loaded]]></Tracking></CustomTracking></Extension></Extensions>
            </InLine>
            </Ad>
            </VAST>
        """
       # print(r)

        result = None
        
        vast = ET.fromstring(r.text)
        for node in vast.iter():
            if node.tag == "MediaFile":
              result = node.text
              break

        print("SHRI :: success GAM")
        return result   
    except Exception as e:
        print("Error in calling GAM")
        print(e)
        # print(traceback.format_exc(), flush=True)
        return None




if __name__ == "__main__":
    callGuaranteedAdServer(None, None)



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