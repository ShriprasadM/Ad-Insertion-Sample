
    ad-transcode:
        image: defn(`REGISTRY_PREFIX')ssai_ad_transcode:latest
        ports:
            - "9008:9008"
        environment:
            NO_PROXY: "*"
            no_proxy: "*"
        volumes:
            - ${AD_CACHE_VOLUME}:/var/www/adinsert:rw
            - ${AD_SEGMENT_VOLUME}:/var/www/adsegment:ro
            - /etc/localtime:/etc/localtime:ro
        networks:
            - appnet
        deploy:
            replicas: defn(`NTRANSCODES')
            placement:
                constraints:
                    - node.role==manager
                    - node.labels.vcac_zone!=yes
