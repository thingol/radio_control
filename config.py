# -*- coding: utf-8 -*-
from collections import OrderedDict

RADIO={"mdr_info":{"display_name":"MDR Info",
        "url":"http://c22033-ls.i.core.cdn.streamfarm.net/QpZptC4ta9922033/22033mdr/live/app2128740352/w2128904192/live_de_128.mp3"},
       "mdr_jump":{"display_name":"MDR Jump",
        "url":"http://c22033-ls.i.core.cdn.streamfarm.net/T3R6XGogC9922033/22033mdr/live/app2128740352/w2128904194/live_de_128.mp3"},
       "mdr_thuer":{"display_name":u"MDR Thüringen",
        "url":"http://c22033-ls.i.core.cdn.streamfarm.net/9lBrdAv9G9922033/22033mdr/live/app2128740352/w2128904199/live_de_128.mp3"},
       "nrk_an":{"display_name":"NRK Alltid Nyheter",
        "url":"http://lyd.nrk.no:80/nrk_radio_alltid_nyheter_aac_h"},
       "nrk_ak":{"display_name":"NRK Alltid Klassisk",
        "url":"http://lyd.nrk.no:80/nrk_radio_klassisk_aac_h"},
       "nrk_p1_trlag":{"display_name":u"NRK P1 Trøndelag",
        "url":"http://lyd.nrk.no/nrk_radio_p1_trondelag_aac_h"},
       "radio_top40":{"display_name":"Radio Top 40",
        "url":"http://xapp2023227392c40000.f.l.i.lb.core-cdn.net/40000mb/live/app2023227392/w2075033610/live_de_128.mp3"}}
RADIO = OrderedDict(sorted(RADIO.items()))

MPD_SRV={"host":"musica.fritz.box",
         "port":6600,
         "passwd":"hubhub"}
