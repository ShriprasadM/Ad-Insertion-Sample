ow_dummy_respose = {'28635736ddc2bb1': [{'pwtbst': '1', 'pwtbst_pubmatic': '1', 'pwtcid': 'c2e0bd69-df7b-45b0-aa95-aeef995cf135', 'pwtcid_pubmatic': 'c2e0bd69-df7b-45b0-aa95-aeef995cf135', 'pwtcpath': '/cache', 'pwtcurl': '//172.16.4.192:2424', 'pwtdid': 'PUBDEAL1', 'pwtdid_pubmatic': 'PUBDEAL1', 'pwtdur': '20', 'pwtecp': '9.00', 'pwtecp_pubmatic': '9.00', 'pwtpid': 'pubmatic', 'pwtpid_pubmatic': 'pubmatic', 'pwtplt': 'video', 'pwtprofid': '2953', 'pwtpubid': '5890', 'pwtsid': '/15671365/MG_VideoAdUnit', 'pwtsid_pubmatic': '/15671365/MG_VideoAdUnit', 'pwtsz': '0x0', 'pwtsz_pubmatic': '0x0', 'pwtverid': '1'}, {'pwtbst': '1', 'pwtbst_pubmatic': '1', 'pwtcid': '265ca7c3-0ec5-4d67-be34-498bc8bc969a', 'pwtcid_pubmatic': '265ca7c3-0ec5-4d67-be34-498bc8bc969a', 'pwtcpath': '/cache', 'pwtcurl': '//172.16.4.192:2424', 'pwtdid': 'PUBDEAL1', 'pwtdid_pubmatic': 'PUBDEAL1', 'pwtdur': '20', 'pwtecp': '9.00', 'pwtecp_pubmatic': '9.00', 'pwtpid': 'pubmatic', 'pwtpid_pubmatic': 'pubmatic', 'pwtplt': 'video', 'pwtprofid': '2953', 'pwtpubid': '5890', 'pwtsid': '/15671365/MG_VideoAdUnit', 'pwtsid_pubmatic': '/15671365/MG_VideoAdUnit', 'pwtsz': '0x0', 'pwtsz_pubmatic': '0x0', 'pwtverid': '1'}, {'pwtbst': '1', 'pwtbst_pubmatic': '1', 'pwtcid': '10a915eb-7e95-4a94-a401-9a841579e3c4', 'pwtcid_pubmatic': '10a915eb-7e95-4a94-a401-9a841579e3c4', 'pwtcpath': '/cache', 'pwtcurl': '//172.16.4.192:2424', 'pwtdid': 'PUBDEAL1', 'pwtdid_pubmatic': 'PUBDEAL1', 'pwtdur': '25', 'pwtecp': '9.00', 'pwtecp_pubmatic': '9.00', 'pwtpid': 'pubmatic', 'pwtpid_pubmatic': 'pubmatic', 'pwtplt': 'video', 'pwtprofid': '2953', 'pwtpubid': '5890', 'pwtsid': '/15671365/MG_VideoAdUnit', 'pwtsid_pubmatic': '/15671365/MG_VideoAdUnit', 'pwtsz': '0x0', 'pwtsz_pubmatic': '0x0', 'pwtverid': '1'}, {'pwtbst': '1', 'pwtbst_pubmatic': '1', 'pwtcid': '0233bdf0-4d98-46ed-ad11-d3a7f3cdffe2', 'pwtcid_pubmatic': '0233bdf0-4d98-46ed-ad11-d3a7f3cdffe2', 'pwtcpath': '/cache', 'pwtcurl': '//172.16.4.192:2424', 'pwtdid': 'PUBDEAL1', 'pwtdid_pubmatic': 'PUBDEAL1', 'pwtdur': '25', 'pwtecp': '9.00', 'pwtecp_pubmatic': '9.00', 'pwtpid': 'pubmatic', 'pwtpid_pubmatic': 'pubmatic', 'pwtplt': 'video', 'pwtprofid': '2953', 'pwtpubid': '5890', 'pwtsid': '/15671365/MG_VideoAdUnit', 'pwtsid_pubmatic': '/15671365/MG_VideoAdUnit', 'pwtsz': '0x0', 'pwtsz_pubmatic': '0x0', 'pwtverid': '1'}]}

# unwrap response example
example2 = """
    {
    "ads": [
        {
            "id": "20001",
            "sequence": null,
            "system": {
                "value": "iabtechlab",
                "version": "4.0"
            },
            "title": "iabtechlab video ad",
            "description": null,
            "advertiser": null,
            "pricing": {
                "value": "25.00",
                "model": "cpm",
                "currency": "USD"
            },
            "survey": null,
            "errorURLTemplates": [
                "http://example.com/error"
            ],
            "impressionURLTemplates": [
                "http://example.com/track/impression"
            ],
            "creatives": [
                {
                    "id": "5480",
                    "adId": null,
                    "sequence": "1",
                    "apiFramework": null,
                    "trackingEvents": {
                        "start": [
                            "http://example.com/tracking/start"
                        ],
                        "firstQuartile": [
                            "http://example.com/tracking/firstQuartile"
                        ],
                        "midpoint": [
                            "http://example.com/tracking/midpoint"
                        ],
                        "thirdQuartile": [
                            "http://example.com/tracking/thirdQuartile"
                        ],
                        "complete": [
                            "http://example.com/tracking/complete"
                        ],
                        "progress-10": [
                            "http://example.com/tracking/progress-10"
                        ]
                    },
                    "type": "linear",
                    "duration": 16,
                    "skipDelay": -1,
                    "mediaFiles": [
                        {
                            "id": "5241",
                            "fileURL": "https://iab-publicfiles.s3.amazonaws.com/vast/VAST-4.0-Short-Intro.mp4",
                            "deliveryType": "progressive",
                            "mimeType": "video/mp4",
                            "codec": "0",
                            "bitrate": 500,
                            "minBitrate": 360,
                            "maxBitrate": 1080,
                            "width": 400,
                            "height": 300,
                            "apiFramework": "",
                            "scalable": null,
                            "maintainAspectRatio": null
                        }
                    ],
                    "videoClickTrackingURLTemplates": [
                        "https://iabtechlab.com"
                    ],
                    "videoCustomClickURLTemplates": [
                        "http://iabtechlab.com"
                    ],
                    "adParameters": null,
                    "icons": []
                }
            ],
            "extensions": [
                {
                    "attributes": {
                        "type": "iab-Count"
                    },
                    "children": [
                        {
                            "name": "total_available",
                            "value": "2",
                            "attributes": {
                                "total_available": null
                            }
                        }
                    ]
                }
            ]
        }
    ],
    "errorURLTemplates": [],
    "version": "3.0"
}
"""
example = """
    {
    "ads": [
        {
            "id": "20004",
            "sequence": null,
            "system": {
                "value": "iabtechlab",
                "version": "4.0"
            },
            "title": "VAST 4.0 Pilot - Scenario 5",
            "description": "This is sample companion ad tag with Linear ad tag. This tag while showing video ad on the player, will show a companion ad beside the player where it can be fitted. At most 3 companion ads can be placed. Modify accordingly to see your own content.",
            "advertiser": null,
            "pricing": {
                "value": "25.00",
                "model": "cpm",
                "currency": "USD"
            },
            "survey": null,
            "errorURLTemplates": [
                "http://example.com/error",
                "http://example.com/error"
            ],
            "impressionURLTemplates": [
                "http://example.com/track/impression",
                "http://example.com/track/impression"
            ],
            "creatives": [
                {
                    "id": "5480",
                    "adId": null,
                    "sequence": "1",
                    "apiFramework": null,
                    "trackingEvents": {},
                    "type": "companion",
                    "variations": [
                        {
                            "id": "1232",
                            "width": "300",
                            "height": "250",
                            "type": "image/png",
                            "staticResource": "https://www.iab.com/wp-content/uploads/2014/09/iab-tech-lab-6-644x290.png",
                            "htmlResource": null,
                            "iframeResource": null,
                            "altText": null,
                            "companionClickThroughURLTemplate": "https://iabtechlab.com",
                            "companionClickTrackingURLTemplates": [],
                            "trackingEvents": {}
                        }
                    ]
                },
                {
                    "id": "5480",
                    "adId": null,
                    "sequence": "1",
                    "apiFramework": null,
                    "trackingEvents": {
                        "start": [
                            "http://example.com/tracking/start"
                        ],
                        "firstQuartile": [
                            "http://example.com/tracking/firstQuartile"
                        ],
                        "midpoint": [
                            "http://example.com/tracking/midpoint"
                        ],
                        "thirdQuartile": [
                            "http://example.com/tracking/thirdQuartile"
                        ],
                        "complete": [
                            "http://example.com/tracking/complete"
                        ],
                        "progress-10": [
                            "http://example.com/tracking/progress-10"
                        ]
                    },
                    "type": "linear",
                    "duration": 16,
                    "skipDelay": -1,
                    "mediaFiles": [
                        {
                            "id": "5241",
                            "fileURL": "https://iab-publicfiles.s3.amazonaws.com/vast/VAST-4.0-Short-Intro.mp4",
                            "deliveryType": "progressive",
                            "mimeType": "video/mp4",
                            "codec": "0",
                            "bitrate": 500,
                            "minBitrate": 360,
                            "maxBitrate": 1080,
                            "width": 400,
                            "height": 300,
                            "apiFramework": "",
                            "scalable": null,
                            "maintainAspectRatio": null
                        },
                         {
                            "id": "5241",
                            "fileURL": "https://iab-publicfiles.s3.amazonaws.com/vast/VAST-4.0-Short-Intro.mp4",
                            "deliveryType": "progressive",
                            "mimeType": "video/mp4",
                            "codec": "0",
                            "bitrate": 500,
                            "minBitrate": 360,
                            "maxBitrate": 1080,
                            "width": 400,
                            "height": 300,
                            "apiFramework": "",
                            "scalable": null,
                            "maintainAspectRatio": null
                        }
                    ],
                    "videoClickTrackingURLTemplates": [
                        "https://iabtechlab.com"
                    ],
                    "videoCustomClickURLTemplates": [],
                    "adParameters": null,
                    "icons": []
                }
            ],
            "extensions": [
                {
                    "attributes": {
                        "type": "iab-Count"
                    },
                    "children": [
                        {
                            "name": "total_available",
                            "value": "2",
                            "attributes": {
                                "total_available": null
                            }
                        }
                    ]
                }
            ]
        }
    ],
    "errorURLTemplates": [],
    "version": "3.0"
}
    """