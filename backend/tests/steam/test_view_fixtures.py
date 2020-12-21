import pytest


@pytest.fixture
def make_game_list_result():
    return {'id': 730, 'tags': [1663, 1774, 3859, 3878, 19, 5711, 5055], 'name': 'Counter-Strike: Global Offensive', 'img_url': ' https://steamcdn-a.akamaihd.net/steam/apps/730/capsule_231x87.jpg', 'release_date': '21 авг. 2012', 'user_review': 'Очень положительные'}


@pytest.fixture
def make_game_list_html_text():
    return """    
    <!-- List Items -->
		<a href="https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/?snr=1_7_7_240_150_1"  data-ds-appid="730" data-ds-itemkey="App_730" data-ds-tagids="[1663,1774,3859,3878,19,5711,5055]" data-ds-descids="[2,5]" data-ds-crtrids="[4]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:730,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/730/capsule_sm_120.jpg?t=1607046958" srcset="https://steamcdn-a.akamaihd.net/steam/apps/730/capsule_sm_120.jpg?t=1607046958 1x, https://steamcdn-a.akamaihd.net/steam/apps/730/capsule_231x87.jpg?t=1607046958 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Counter-Strike: Global Offensive</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">21 авг. 2012</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;88% из 5,102,917 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="102000">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        Бесплатно                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/570/Dota_2/?snr=1_7_7_240_150_1"  data-ds-appid="570" data-ds-itemkey="App_570" data-ds-tagids="[113,1718,3859,9,5055,5711,3878]" data-ds-crtrids="[4]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:570,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/570/capsule_sm_120.jpg?t=1608341990" srcset="https://steamcdn-a.akamaihd.net/steam/apps/570/capsule_sm_120.jpg?t=1608341990 1x, https://steamcdn-a.akamaihd.net/steam/apps/570/capsule_231x87.jpg?t=1608341990 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Dota 2</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span><span class="vr_supported">Поддержка VR</span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">9 июл. 2013</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;84% из 1,425,294 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="0">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        Бесплатно                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/582010/Monster_Hunter_World/?snr=1_7_7_240_150_1"  data-ds-appid="582010" data-ds-itemkey="App_582010" data-ds-tagids="[1685,3859,19,1695,122,1697,4747]" data-ds-crtrids="[33273264,34827959]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:582010,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/582010/capsule_sm_120.jpg?t=1602806745" srcset="https://steamcdn-a.akamaihd.net/steam/apps/582010/capsule_sm_120.jpg?t=1602806745 1x, https://steamcdn-a.akamaihd.net/steam/apps/582010/capsule_231x87.jpg?t=1602806745 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Monster Hunter: World</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">9 авг. 2018</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;84% из 173,164 обзоров положительные.&lt;br&gt;&lt;br&gt;Замечены периоды обзоров не по теме. Учитывая ваши настройки, мы исключили эти обзоры из общего рейтинга.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="99900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        999 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/578080/PLAYERUNKNOWNS_BATTLEGROUNDS/?snr=1_7_7_240_150_1"  data-ds-appid="578080" data-ds-itemkey="App_578080" data-ds-tagids="[1662,1774,3859,176981,1663,1775,3814]" data-ds-descids="[2,5]" data-ds-crtrids="[33973721]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:578080,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/578080/capsule_sm_120.jpg?t=1608093288" srcset="https://steamcdn-a.akamaihd.net/steam/apps/578080/capsule_sm_120.jpg?t=1608093288 1x, https://steamcdn-a.akamaihd.net/steam/apps/578080/capsule_231x87.jpg?t=1608093288 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">PLAYERUNKNOWN'S BATTLEGROUNDS</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">21 дек. 2017</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary mixed" data-tooltip-html="Смешанные&lt;br&gt;52% из 1,354,830 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="94900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        949 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/457140/Oxygen_Not_Included/?snr=1_7_7_240_150_1"  data-ds-appid="457140" data-ds-itemkey="App_457140" data-ds-tagids="[220585,7332,1662,8945,1643,4182,599]" data-ds-crtrids="[112393]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:457140,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/457140/capsule_sm_120.jpg?t=1608323271" srcset="https://steamcdn-a.akamaihd.net/steam/apps/457140/capsule_sm_120.jpg?t=1608323271 1x, https://steamcdn-a.akamaihd.net/steam/apps/457140/capsule_231x87.jpg?t=1608323271 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Oxygen Not Included</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">30 июл. 2019</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;96% из 53,137 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="22400">
                    <div class="col search_discount responsive_secondrow">
                        <span>-50%</span>
                    </div>
                    <div class="col search_price discounted responsive_secondrow">
                        <span style="color: #888888;"><strike>449 pуб.</strike></span><br>224 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/381210/Dead_by_Daylight/?snr=1_7_7_240_150_1"  data-ds-appid="381210" data-ds-itemkey="App_381210" data-ds-tagids="[1667,3978,3859,3843,1662,1687,4345]" data-ds-descids="[2,5]" data-ds-crtrids="[32824912]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:381210,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/381210/capsule_sm_120.jpg?t=1606845070" srcset="https://steamcdn-a.akamaihd.net/steam/apps/381210/capsule_sm_120.jpg?t=1606845070 1x, https://steamcdn-a.akamaihd.net/steam/apps/381210/capsule_231x87.jpg?t=1606845070 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Dead by Daylight</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">14 июн. 2016</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;82% из 296,925 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="49900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        499 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/952060/Resident_Evil_3/?snr=1_7_7_240_150_1"  data-ds-appid="952060" data-ds-itemkey="App_952060" data-ds-tagids="[19,1659,1667,7208,3859,3978,5708]" data-ds-descids="[2,5]" data-ds-crtrids="[33273264,34827950]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:952060,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/952060/capsule_sm_120.jpg?t=1608229289" srcset="https://steamcdn-a.akamaihd.net/steam/apps/952060/capsule_sm_120.jpg?t=1608229289 1x, https://steamcdn-a.akamaihd.net/steam/apps/952060/capsule_231x87.jpg?t=1608229289 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Resident Evil 3</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">2 апр. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="В основном положительные&lt;br&gt;74% из 24,731 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="65967">
                    <div class="col search_discount responsive_secondrow">
                        <span>-67%</span>
                    </div>
                    <div class="col search_price discounted responsive_secondrow">
                        <span style="color: #888888;"><strike>1999 pуб.</strike></span><br>659,67 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/1097150/Fall_Guys_Ultimate_Knockout/?snr=1_7_7_240_150_1"  data-ds-appid="1097150" data-ds-itemkey="App_1097150" data-ds-tagids="[3859,4136,176981,3843,5350,1719,7178]" data-ds-crtrids="[38424069,6638525]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:1097150,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/1097150/capsule_sm_120_alt_assets_2.jpg?t=1608408819" srcset="https://steamcdn-a.akamaihd.net/steam/apps/1097150/capsule_sm_120_alt_assets_2.jpg?t=1608408819 1x, https://steamcdn-a.akamaihd.net/steam/apps/1097150/capsule_231x87_alt_assets_2.jpg?t=1608408819 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Fall Guys: Ultimate Knockout</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">3 авг. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;82% из 287,381 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="46500">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        465 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/1145360/Hades/?snr=1_7_7_240_150_1"  data-ds-appid="1145360" data-ds-itemkey="App_1145360" data-ds-tagids="[42804,19,492,122,3959,1646,1720]" data-ds-crtrids="[3584665]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:1145360,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/1145360/capsule_sm_120.jpg?t=1606329416" srcset="https://steamcdn-a.akamaihd.net/steam/apps/1145360/capsule_sm_120.jpg?t=1606329416 1x, https://steamcdn-a.akamaihd.net/steam/apps/1145360/capsule_231x87.jpg?t=1606329416 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Hades</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">17 сен. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;98% из 92,099 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="46500">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        465 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/1118010/Monster_Hunter_World_Iceborne/?snr=1_7_7_240_150_1"  data-ds-appid="1118010" data-ds-itemkey="App_1118010" data-ds-tagids="[19,3859,1695,1685,9564,4026,1697]" data-ds-crtrids="[33273264,34827959]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:1118010,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/1118010/capsule_sm_120.jpg?t=1605143784" srcset="https://steamcdn-a.akamaihd.net/steam/apps/1118010/capsule_sm_120.jpg?t=1605143784 1x, https://steamcdn-a.akamaihd.net/steam/apps/1118010/capsule_231x87.jpg?t=1605143784 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Monster Hunter World: Iceborne</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">9 янв. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary mixed" data-tooltip-html="Смешанные&lt;br&gt;51% из 12,962 обзоров положительные.&lt;br&gt;&lt;br&gt;Замечены периоды обзоров не по теме. Учитывая ваши настройки, мы исключили эти обзоры из общего рейтинга.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="129900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1299 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/322330/Dont_Starve_Together/?snr=1_7_7_240_150_1"  data-ds-appid="322330" data-ds-itemkey="App_322330" data-ds-tagids="[1662,1100689,3859,1685,1695,21,1702]" data-ds-crtrids="[112393]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:322330,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/322330/capsule_sm_120_alt_assets_0.jpg?t=1608060905" srcset="https://steamcdn-a.akamaihd.net/steam/apps/322330/capsule_sm_120_alt_assets_0.jpg?t=1608060905 1x, https://steamcdn-a.akamaihd.net/steam/apps/322330/capsule_231x87_alt_assets_0.jpg?t=1608060905 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Don't Starve Together</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">21 апр. 2016</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;96% из 146,154 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="11800">
                    <div class="col search_discount responsive_secondrow">
                        <span>-66%</span>
                    </div>
                    <div class="col search_price discounted responsive_secondrow">
                        <span style="color: #888888;"><strike>349 pуб.</strike></span><br>118 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/794260/Outward/?snr=1_7_7_240_150_1"  data-ds-appid="794260" data-ds-itemkey="App_794260" data-ds-tagids="[122,1695,1662,1685,3843,1684,21]" data-ds-descids="[2,5]" data-ds-crtrids="[4283115]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:794260,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/794260/capsule_sm_120.jpg?t=1608035082" srcset="https://steamcdn-a.akamaihd.net/steam/apps/794260/capsule_sm_120.jpg?t=1608035082 1x, https://steamcdn-a.akamaihd.net/steam/apps/794260/capsule_231x87.jpg?t=1608035082 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Outward</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">26 мар. 2019</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="В основном положительные&lt;br&gt;75% из 10,810 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="35900">
                    <div class="col search_discount responsive_secondrow">
                        <span>-70%</span>
                    </div>
                    <div class="col search_price discounted responsive_secondrow">
                        <span style="color: #888888;"><strike>1199 pуб.</strike></span><br>359 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/1139900/Ghostrunner/?snr=1_7_7_240_150_1"  data-ds-appid="1139900" data-ds-itemkey="App_1139900" data-ds-tagids="[19,4115,3839,1734,4295,4182,4608]" data-ds-descids="[2,5]" data-ds-crtrids="[5161,33032949,34306834,33027220]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:1139900,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/1139900/capsule_sm_120.jpg?t=1608227815" srcset="https://steamcdn-a.akamaihd.net/steam/apps/1139900/capsule_sm_120.jpg?t=1608227815 1x, https://steamcdn-a.akamaihd.net/steam/apps/1139900/capsule_231x87.jpg?t=1608227815 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Ghostrunner</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">27 окт. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;91% из 13,389 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="112400">
                    <div class="col search_discount responsive_secondrow">
                        <span>-25%</span>
                    </div>
                    <div class="col search_price discounted responsive_secondrow">
                        <span style="color: #888888;"><strike>1499 pуб.</strike></span><br>1124 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/359320/Elite_Dangerous/?snr=1_7_7_240_150_1"  data-ds-appid="359320" data-ds-itemkey="App_359320" data-ds-tagids="[16598,1755,1695,3834,3942,599,128]" data-ds-crtrids="[26299579]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:359320,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/359320/capsule_sm_120.jpg?t=1603796492" srcset="https://steamcdn-a.akamaihd.net/steam/apps/359320/capsule_sm_120.jpg?t=1603796492 1x, https://steamcdn-a.akamaihd.net/steam/apps/359320/capsule_231x87.jpg?t=1603796492 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Elite Dangerous</span>
                    <p>
                        <span class="platform_img win"></span><span class="vr_supported">Поддержка VR</span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">2 апр. 2015</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="В основном положительные&lt;br&gt;76% из 48,256 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="99900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        999 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/601150/Devil_May_Cry_5/?snr=1_7_7_240_150_1"  data-ds-appid="601150" data-ds-itemkey="App_601150" data-ds-tagids="[19,1646,1756,9541,3955,4777,1697]" data-ds-descids="[1,2,5]" data-ds-crtrids="[33273264,34827954]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:601150,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/601150/capsule_sm_120.jpg?t=1607993615" srcset="https://steamcdn-a.akamaihd.net/steam/apps/601150/capsule_sm_120.jpg?t=1607993615 1x, https://steamcdn-a.akamaihd.net/steam/apps/601150/capsule_231x87.jpg?t=1607993615 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Devil May Cry 5</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">7 мар. 2019</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;93% из 30,651 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="149900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1499 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/782330/DOOM_Eternal/?snr=1_7_7_240_150_1"  data-ds-appid="782330" data-ds-itemkey="App_782330" data-ds-tagids="[19,1663,1756,4345,9541,4667,1734]" data-ds-descids="[2,5]" data-ds-crtrids="[33028765,35501448]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:782330,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/782330/capsule_sm_120.jpg?t=1603213568" srcset="https://steamcdn-a.akamaihd.net/steam/apps/782330/capsule_sm_120.jpg?t=1603213568 1x, https://steamcdn-a.akamaihd.net/steam/apps/782330/capsule_231x87.jpg?t=1603213568 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">DOOM Eternal</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">19 мар. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;89% из 88,311 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="199900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1999 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/883710/Resident_Evil_2/?snr=1_7_7_240_150_1"  data-ds-appid="883710" data-ds-itemkey="App_883710" data-ds-tagids="[1659,3978,1667,5708,4182,1697,4345]" data-ds-descids="[2,5]" data-ds-crtrids="[33273264,34827950]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:883710,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/883710/capsule_sm_120.jpg?t=1591585395" srcset="https://steamcdn-a.akamaihd.net/steam/apps/883710/capsule_sm_120.jpg?t=1591585395 1x, https://steamcdn-a.akamaihd.net/steam/apps/883710/capsule_231x87.jpg?t=1591585395 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Resident Evil 2</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">24 янв. 2019</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;97% из 50,707 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="159900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1599 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/814380/Sekiro_Shadows_Die_Twice__GOTY_Edition/?snr=1_7_7_240_150_1"  data-ds-appid="814380" data-ds-itemkey="App_814380" data-ds-tagids="[29482,4026,19,4182,1688,1687,21]" data-ds-descids="[2,5]" data-ds-crtrids="[33770678]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:814380,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/814380/capsule_sm_120.jpg?t=1603904569" srcset="https://steamcdn-a.akamaihd.net/steam/apps/814380/capsule_sm_120.jpg?t=1603904569 1x, https://steamcdn-a.akamaihd.net/steam/apps/814380/capsule_231x87.jpg?t=1603904569 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Sekiro™: Shadows Die Twice - GOTY Edition</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">21 мар. 2019</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;94% из 78,909 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="199900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1999 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/493520/GTFO/?snr=1_7_7_240_150_1"  data-ds-appid="493520" data-ds-itemkey="App_493520" data-ds-tagids="[493,1667,3843,19,3859,1663,1685]" data-ds-descids="[2,5]" data-ds-crtrids="[34697516]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:493520,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/493520/capsule_sm_120.jpg?t=1608157589" srcset="https://steamcdn-a.akamaihd.net/steam/apps/493520/capsule_sm_120.jpg?t=1608157589 1x, https://steamcdn-a.akamaihd.net/steam/apps/493520/capsule_231x87.jpg?t=1608157589 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">GTFO</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">9 дек. 2019</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;88% из 16,038 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="95920">
                    <div class="col search_discount responsive_secondrow">
                        <span>-20%</span>
                    </div>
                    <div class="col search_price discounted responsive_secondrow">
                        <span style="color: #888888;"><strike>1199 pуб.</strike></span><br>959,20 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/232090/Killing_Floor_2/?snr=1_7_7_240_150_1"  data-ds-appid="232090" data-ds-itemkey="App_232090" data-ds-tagids="[1659,1685,4345,1663,1662,3859,19]" data-ds-crtrids="[32797243]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:232090,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/232090/capsule_sm_120.jpg?t=1608053967" srcset="https://steamcdn-a.akamaihd.net/steam/apps/232090/capsule_sm_120.jpg?t=1608053967 1x, https://steamcdn-a.akamaihd.net/steam/apps/232090/capsule_231x87.jpg?t=1608053967 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Killing Floor 2</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">18 ноя. 2016</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;88% из 64,913 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="29600">
                    <div class="col search_discount responsive_secondrow">
                        <span>-67%</span>
                    </div>
                    <div class="col search_price discounted responsive_secondrow">
                        <span style="color: #888888;"><strike>899 pуб.</strike></span><br>296 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/881100/Noita/?snr=1_7_7_240_150_1"  data-ds-appid="881100" data-ds-itemkey="App_881100" data-ds-tagids="[19,1720,1716,492,122,42804,4026]" data-ds-crtrids="[35664460]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:881100,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/881100/capsule_sm_120_alt_assets_2.jpg?t=1604678843" srcset="https://steamcdn-a.akamaihd.net/steam/apps/881100/capsule_sm_120_alt_assets_2.jpg?t=1604678843 1x, https://steamcdn-a.akamaihd.net/steam/apps/881100/capsule_231x87_alt_assets_2.jpg?t=1604678843 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Noita</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">15 окт. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;95% из 21,971 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="43500">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        435 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/265300/Lords_Of_The_Fallen/?snr=1_7_7_240_150_1"  data-ds-appid="265300" data-ds-itemkey="App_265300" data-ds-tagids="[29482,122,19,4604,4231,4182,4026]" data-ds-crtrids="[32970584]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:265300,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/265300/capsule_sm_120.jpg?t=1605004665" srcset="https://steamcdn-a.akamaihd.net/steam/apps/265300/capsule_sm_120.jpg?t=1605004665 1x, https://steamcdn-a.akamaihd.net/steam/apps/265300/capsule_231x87.jpg?t=1605004665 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Lords Of The Fallen™</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">28 окт. 2014</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary mixed" data-tooltip-html="Смешанные&lt;br&gt;59% из 9,248 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="4990">
                    <div class="col search_discount responsive_secondrow">
                        <span>-90%</span>
                    </div>
                    <div class="col search_price discounted responsive_secondrow">
                        <span style="color: #888888;"><strike>499 pуб.</strike></span><br>49,90 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/620980/Beat_Saber/?snr=1_7_7_240_150_1"  data-ds-appid="620980" data-ds-itemkey="App_620980" data-ds-tagids="[21978,1752,1621,1756,492,1734,4182]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:620980,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/620980/capsule_sm_120_alt_assets_1.jpg?t=1605633883" srcset="https://steamcdn-a.akamaihd.net/steam/apps/620980/capsule_sm_120_alt_assets_1.jpg?t=1605633883 1x, https://steamcdn-a.akamaihd.net/steam/apps/620980/capsule_231x87_alt_assets_1.jpg?t=1605633883 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Beat Saber</span>
                    <p>
                        <span class="platform_img win"></span><span class="vr_required">Только VR</span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">21 мая. 2019</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;96% из 40,115 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="51500">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        515 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/250900/The_Binding_of_Isaac_Rebirth/?snr=1_7_7_240_150_1"  data-ds-appid="250900" data-ds-itemkey="App_250900" data-ds-tagids="[42804,1716,492,4711,4026,3964,1720]" data-ds-crtrids="[33060864,3200829]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:250900,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/250900/capsule_sm_120.jpg?t=1573181772" srcset="https://steamcdn-a.akamaihd.net/steam/apps/250900/capsule_sm_120.jpg?t=1573181772 1x, https://steamcdn-a.akamaihd.net/steam/apps/250900/capsule_231x87.jpg?t=1573181772 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">The Binding of Isaac: Rebirth</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">4 ноя. 2014</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;98% из 104,745 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="44900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        449 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/1356670/Sakuna_Of_Rice_and_Ruin/?snr=1_7_7_240_150_1"  data-ds-appid="1356670" data-ds-itemkey="App_1356670" data-ds-tagids="[19,87918,1742,3798,1625,16094,7208]" data-ds-crtrids="[33144221]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:1356670,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/1356670/capsule_sm_120.jpg?t=1606328072" srcset="https://steamcdn-a.akamaihd.net/steam/apps/1356670/capsule_sm_120.jpg?t=1606328072 1x, https://steamcdn-a.akamaihd.net/steam/apps/1356670/capsule_231x87.jpg?t=1606328072 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Sakuna: Of Rice and Ruin</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">10 ноя. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;94% из 1,819 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="72500">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        725 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/581320/Insurgency_Sandstorm/?snr=1_7_7_240_150_1"  data-ds-appid="581320" data-ds-itemkey="App_581320" data-ds-tagids="[1663,4175,1774,19,4168,3859,1708]" data-ds-descids="[2,5]" data-ds-crtrids="[33031377,21394]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:581320,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/581320/capsule_sm_120.jpg?t=1607553229" srcset="https://steamcdn-a.akamaihd.net/steam/apps/581320/capsule_sm_120.jpg?t=1607553229 1x, https://steamcdn-a.akamaihd.net/steam/apps/581320/capsule_231x87.jpg?t=1607553229 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Insurgency: Sandstorm</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">12 дек. 2018</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;84% из 48,414 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="99900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        999 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/374320/DARK_SOULS_III/?snr=1_7_7_240_150_1"  data-ds-appid="374320" data-ds-itemkey="App_374320" data-ds-tagids="[29482,4604,4026,122,4166,3854,1697]" data-ds-crtrids="[33042543]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:374320,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/374320/capsule_sm_120.jpg?t=1608544497" srcset="https://steamcdn-a.akamaihd.net/steam/apps/374320/capsule_sm_120.jpg?t=1608544497 1x, https://steamcdn-a.akamaihd.net/steam/apps/374320/capsule_231x87.jpg?t=1608544497 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">DARK SOULS™ III</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">11 апр. 2016</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;93% из 147,553 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="199900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1999 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/1057090/Ori_and_the_Will_of_the_Wisps/?snr=1_7_7_240_150_1"  data-ds-appid="1057090" data-ds-itemkey="App_1057090" data-ds-tagids="[5411,1628,1756,19,1625,4182,4166]" data-ds-crtrids="[37856651,3090835]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:1057090,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/1057090/capsule_sm_120.jpg?t=1605538811" srcset="https://steamcdn-a.akamaihd.net/steam/apps/1057090/capsule_sm_120.jpg?t=1605538811 1x, https://steamcdn-a.akamaihd.net/steam/apps/1057090/capsule_231x87.jpg?t=1605538811 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Ori and the Will of the Wisps</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">10 мар. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;95% из 43,659 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="51500">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        515 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/323190/Frostpunk/?snr=1_7_7_240_150_1"  data-ds-appid="323190" data-ds-itemkey="App_323190" data-ds-tagids="[1662,4328,9,8945,3835,1777,220585]" data-ds-crtrids="[32989971]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:323190,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/323190/capsule_sm_120.jpg?t=1603983228" srcset="https://steamcdn-a.akamaihd.net/steam/apps/323190/capsule_sm_120.jpg?t=1603983228 1x, https://steamcdn-a.akamaihd.net/steam/apps/323190/capsule_231x87.jpg?t=1603983228 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Frostpunk</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">24 апр. 2018</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;90% из 48,387 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="59900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        599 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/367520/Hollow_Knight/?snr=1_7_7_240_150_1"  data-ds-appid="367520" data-ds-itemkey="App_367520" data-ds-tagids="[1628,29482,1625,1756,4026,3871,492]" data-ds-crtrids="[33040195]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:367520,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/367520/capsule_sm_120.jpg?t=1601950406" srcset="https://steamcdn-a.akamaihd.net/steam/apps/367520/capsule_sm_120.jpg?t=1601950406 1x, https://steamcdn-a.akamaihd.net/steam/apps/367520/capsule_231x87.jpg?t=1601950406 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Hollow Knight</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">24 фев. 2017</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;96% из 110,702 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="34900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        349 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/411300/ELEX/?snr=1_7_7_240_150_1"  data-ds-appid="411300" data-ds-itemkey="App_411300" data-ds-tagids="[122,1695,4182,3835,3942,1684,21]" data-ds-crtrids="[36223093,7564110]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:411300,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/411300/capsule_sm_120.jpg?t=1590128223" srcset="https://steamcdn-a.akamaihd.net/steam/apps/411300/capsule_sm_120.jpg?t=1590128223 1x, https://steamcdn-a.akamaihd.net/steam/apps/411300/capsule_231x87.jpg?t=1590128223 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">ELEX</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">17 окт. 2017</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="В основном положительные&lt;br&gt;72% из 8,383 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="34900">
                    <div class="col search_discount responsive_secondrow">
                        <span>-75%</span>
                    </div>
                    <div class="col search_price discounted responsive_secondrow">
                        <span style="color: #888888;"><strike>1399 pуб.</strike></span><br>349 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/268910/Cuphead/?snr=1_7_7_240_150_1"  data-ds-appid="268910" data-ds-itemkey="App_268910" data-ds-tagids="[4026,4562,1625,1756,1685,6815,3841]" data-ds-crtrids="[32949938]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:268910,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/268910/capsule_sm_120.jpg?t=1589281999" srcset="https://steamcdn-a.akamaihd.net/steam/apps/268910/capsule_sm_120.jpg?t=1589281999 1x, https://steamcdn-a.akamaihd.net/steam/apps/268910/capsule_231x87.jpg?t=1589281999 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Cuphead</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">29 сен. 2017</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;96% из 57,525 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="41900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        419 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/219740/Dont_Starve/?snr=1_7_7_240_150_1"  data-ds-appid="219740" data-ds-itemkey="App_219740" data-ds-tagids="[1662,1100689,1702,21,492,3810,4182]" data-ds-crtrids="[112393]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:219740,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/219740/capsule_sm_120.jpg?t=1602117150" srcset="https://steamcdn-a.akamaihd.net/steam/apps/219740/capsule_sm_120.jpg?t=1602117150 1x, https://steamcdn-a.akamaihd.net/steam/apps/219740/capsule_231x87.jpg?t=1602117150 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Don't Starve</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow"></div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;96% из 68,521 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="25900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        259 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/870780/Control_Ultimate_Edition/?snr=1_7_7_240_150_1"  data-ds-appid="870780" data-ds-itemkey="App_870780" data-ds-tagids="[19,21,7208,10808,3942,1697,1742]" data-ds-descids="[2,5]" data-ds-crtrids="[34087437,33027220]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:870780,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/870780/capsule_sm_120.jpg?t=1604045960" srcset="https://steamcdn-a.akamaihd.net/steam/apps/870780/capsule_sm_120.jpg?t=1604045960 1x, https://steamcdn-a.akamaihd.net/steam/apps/870780/capsule_231x87.jpg?t=1604045960 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Control Ultimate Edition</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">27 авг. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;91% из 9,288 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="159900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1599 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/262060/Darkest_Dungeon/?snr=1_7_7_240_150_1"  data-ds-appid="262060" data-ds-itemkey="App_262060" data-ds-tagids="[4325,4604,1720,122,1716,7432,4026]" data-ds-crtrids="[32946145]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:262060,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/262060/capsule_sm_120.jpg?t=1598289046" srcset="https://steamcdn-a.akamaihd.net/steam/apps/262060/capsule_sm_120.jpg?t=1598289046 1x, https://steamcdn-a.akamaihd.net/steam/apps/262060/capsule_231x87.jpg?t=1598289046 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Darkest Dungeon®</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">19 янв. 2016</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;90% из 73,234 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="44900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        449 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/632360/Risk_of_Rain_2/?snr=1_7_7_240_150_1"  data-ds-appid="632360" data-ds-itemkey="App_632360" data-ds-tagids="[3814,42804,3859,19,3959,1685,353880]" data-ds-crtrids="[35646051]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:632360,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/632360/capsule_sm_120.jpg?t=1597330177" srcset="https://steamcdn-a.akamaihd.net/steam/apps/632360/capsule_sm_120.jpg?t=1597330177 1x, https://steamcdn-a.akamaihd.net/steam/apps/632360/capsule_231x87.jpg?t=1597330177 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Risk of Rain 2</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">11 авг. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;96% из 89,872 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="79900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        799 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/774861/Project_Winter/?snr=1_7_7_240_150_1"  data-ds-appid="774861" data-ds-itemkey="App_774861" data-ds-tagids="[745697,1662,3859,5711,492,3843,1685]" data-ds-descids="[5]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:774861,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/774861/capsule_sm_120.jpg?t=1608139018" srcset="https://steamcdn-a.akamaihd.net/steam/apps/774861/capsule_sm_120.jpg?t=1608139018 1x, https://steamcdn-a.akamaihd.net/steam/apps/774861/capsule_231x87.jpg?t=1608139018 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Project Winter</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">23 мая. 2019</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;86% из 10,086 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="43500">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        435 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/257420/Serious_Sam_4/?snr=1_7_7_240_150_1"  data-ds-appid="257420" data-ds-itemkey="App_257420" data-ds-tagids="[19,4345,1663,1774,1685,21,4667]" data-ds-descids="[2,5]" data-ds-crtrids="[33025992,6638525,37439254]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:257420,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/257420/capsule_sm_120.jpg?t=1606304017" srcset="https://steamcdn-a.akamaihd.net/steam/apps/257420/capsule_sm_120.jpg?t=1606304017 1x, https://steamcdn-a.akamaihd.net/steam/apps/257420/capsule_231x87.jpg?t=1606304017 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Serious Sam 4</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">24 сен. 2020</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;84% из 7,190 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="72500">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        725 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/761890/Albion_Online/?snr=1_7_7_240_150_1"  data-ds-appid="761890" data-ds-itemkey="App_761890" data-ds-tagids="[113,1754,128,1695,122,3810,1702]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:761890,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/761890/capsule_sm_120.jpg?t=1606139494" srcset="https://steamcdn-a.akamaihd.net/steam/apps/761890/capsule_sm_120.jpg?t=1606139494 1x, https://steamcdn-a.akamaihd.net/steam/apps/761890/capsule_231x87.jpg?t=1606139494 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Albion Online</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">16 мая. 2018</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="В основном положительные&lt;br&gt;77% из 26,202 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="0">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        Бесплатно                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/570940/DARK_SOULS_REMASTERED/?snr=1_7_7_240_150_1"  data-ds-appid="570940" data-ds-itemkey="App_570940" data-ds-tagids="[29482,4604,19,4342,122,4026,1684]" data-ds-crtrids="[33042543]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:570940,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/570940/capsule_sm_120.jpg?t=1605604948" srcset="https://steamcdn-a.akamaihd.net/steam/apps/570940/capsule_sm_120.jpg?t=1605604948 1x, https://steamcdn-a.akamaihd.net/steam/apps/570940/capsule_231x87.jpg?t=1605604948 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">DARK SOULS™: REMASTERED</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">23 мая. 2018</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;83% из 24,323 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="119900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1199 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div> </a> <a 
            href="https://store.steampowered.com/app/8500/EVE_Online/?snr=1_7_7_240_150_1"  data-ds-appid="8500" 
            data-ds-itemkey="App_8500" data-ds-tagids="[1755,128,3942,113,122,3810,1754]" data-ds-crtrids="[10551]" 
            onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,
            &quot;id&quot;:8500,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 
            'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" > <div class="col 
            search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/8500/capsule_sm_120.jpg?t=1607532853
            " srcset="https://steamcdn-a.akamaihd.net/steam/apps/8500/capsule_sm_120.jpg?t=1607532853 1x, 
            https://steamcdn-a.akamaihd.net/steam/apps/8500/capsule_231x87.jpg?t=1607532853 2x"></div> <div 
            class="responsive_search_name_combined"> <div class="col search_name ellipsis"> <span class="title">EVE 
            Online</span> <p> <span class="platform_img win"></span><span class="platform_img mac"></span>            
                    </p> </div> <div class="col search_released responsive_secondrow">15 дек. 2010</div> <div 
                    class="col search_reviewscore responsive_secondrow"> <span class="search_review_summary positive" 
                    data-tooltip-html="В основном положительные&lt;br&gt;76% из 21,061 обзоров положительные."> 
                    </span> </div> 


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="0">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        Бесплатно                    </div>
                </div>
            </div>


            <div style="clear: left;"></div> </a> <a href="https://store.steampowered.com/app/263280/Spintires/?snr
            =1_7_7_240_150_1"  data-ds-appid="263280" data-ds-itemkey="App_263280" data-ds-tagids="[599,7622,1100687,
            3968,3859,1644,4175]" data-ds-crtrids="[35726398]" onmouseover="GameHover( this, event, 'global_hover', 
            {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:263280,&quot;public&quot;:1,&quot;v6&quot;:1} );" 
            onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " 
            data-search-page="1" > <div class="col search_capsule"><img 
            src="https://steamcdn-a.akamaihd.net/steam/apps/263280/capsule_sm_120.jpg?t=1607908074" 
            srcset="https://steamcdn-a.akamaihd.net/steam/apps/263280/capsule_sm_120.jpg?t=1607908074 1x, 
            https://steamcdn-a.akamaihd.net/steam/apps/263280/capsule_231x87.jpg?t=1607908074 2x"></div> <div 
            class="responsive_search_name_combined"> <div class="col search_name ellipsis"> <span 
            class="title">Spintires®</span> <p> <span class="platform_img win"></span>                    </p> </div> 
            <div class="col search_released responsive_secondrow">12 июн. 2014</div> <div class="col 
            search_reviewscore responsive_secondrow"> <span class="search_review_summary positive" 
            data-tooltip-html="Очень положительные&lt;br&gt;87% из 19,787 обзоров положительные."> </span> </div> 


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="28900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        289 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div> </a> <a 
            href="https://store.steampowered.com/app/389730/TEKKEN_7/?snr=1_7_7_240_150_1"  data-ds-appid="389730" 
            data-ds-itemkey="App_389730" data-ds-tagids="[1743,19,3859,3878,1773,7368,701]" data-ds-crtrids="[
            33042543]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,
            &quot;id&quot;:389730,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 
            'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" > <div class="col 
            search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/389730/capsule_sm_120.jpg?t
            =1604997008" srcset="https://steamcdn-a.akamaihd.net/steam/apps/389730/capsule_sm_120.jpg?t=1604997008 
            1x, https://steamcdn-a.akamaihd.net/steam/apps/389730/capsule_231x87.jpg?t=1604997008 2x"></div> <div 
            class="responsive_search_name_combined"> <div class="col search_name ellipsis"> <span 
            class="title">TEKKEN 7</span> <p> <span class="platform_img win"></span>                    </p> </div> 
            <div class="col search_released responsive_secondrow">1 июн. 2017</div> <div class="col 
            search_reviewscore responsive_secondrow"> <span class="search_review_summary positive" 
            data-tooltip-html="Очень положительные&lt;br&gt;83% из 28,628 обзоров положительные."> </span> </div> 


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="119900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1199 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/326360/Warspear_Online/?snr=1_7_7_240_150_1"  data-ds-appid="326360" data-ds-itemkey="App_326360" data-ds-tagids="[113,3964,1754,128,122,3859,4026]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:326360,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/326360/capsule_sm_120.jpg?t=1601895674" srcset="https://steamcdn-a.akamaihd.net/steam/apps/326360/capsule_sm_120.jpg?t=1601895674 1x, https://steamcdn-a.akamaihd.net/steam/apps/326360/capsule_231x87.jpg?t=1601895674 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Warspear Online</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">2 ноя. 2017</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="В основном положительные&lt;br&gt;75% из 1,508 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="0">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        Бесплатно                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/268500/XCOM_2/?snr=1_7_7_240_150_1"  data-ds-appid="268500" data-ds-itemkey="App_268500" data-ds-tagids="[9,1677,1708,1741,1673,14139,3942]" data-ds-crtrids="[32844624,33824648,2428135,33339602]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:268500,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/268500/capsule_sm_120.jpg?t=1600177724" srcset="https://steamcdn-a.akamaihd.net/steam/apps/268500/capsule_sm_120.jpg?t=1600177724 1x, https://steamcdn-a.akamaihd.net/steam/apps/268500/capsule_231x87.jpg?t=1600177724 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">XCOM® 2</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">4 фев. 2016</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;86% из 41,382 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="169900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1699 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/4500/STALKER_Shadow_of_Chernobyl/?snr=1_7_7_240_150_1"  data-ds-appid="4500" data-ds-itemkey="App_4500" data-ds-tagids="[4166,3835,1695,1663,1662,19,122]" data-ds-crtrids="[33676874,6313]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:4500,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/4500/capsule_sm_120.jpg?t=1599052748" srcset="https://steamcdn-a.akamaihd.net/steam/apps/4500/capsule_sm_120.jpg?t=1599052748 1x, https://steamcdn-a.akamaihd.net/steam/apps/4500/capsule_231x87.jpg?t=1599052748 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">S.T.A.L.K.E.R.: Shadow of Chernobyl</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">20 мар. 2007</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;95% из 14,525 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="59900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        599 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/508440/Totally_Accurate_Battle_Simulator/?snr=1_7_7_240_150_1"  data-ds-appid="508440" data-ds-itemkey="App_508440" data-ds-tagids="[599,4136,3810,1678,9,4182,19]" data-ds-crtrids="[32941859]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:508440,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/508440/capsule_sm_120.jpg?t=1590572381" srcset="https://steamcdn-a.akamaihd.net/steam/apps/508440/capsule_sm_120.jpg?t=1590572381 1x, https://steamcdn-a.akamaihd.net/steam/apps/508440/capsule_231x87.jpg?t=1590572381 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Totally Accurate Battle Simulator</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">1 апр. 2019</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Крайне положительные&lt;br&gt;98% из 45,962 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="36000">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        360 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/220200/Kerbal_Space_Program/?snr=1_7_7_240_150_1"  data-ds-appid="220200" data-ds-itemkey="App_220200" data-ds-tagids="[1755,599,3810,3968,5794,16598,1643]" data-ds-crtrids="[34024188]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:220200,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/220200/capsule_sm_120.jpg?t=1604087386" srcset="https://steamcdn-a.akamaihd.net/steam/apps/220200/capsule_sm_120.jpg?t=1604087386 1x, https://steamcdn-a.akamaihd.net/steam/apps/220200/capsule_231x87.jpg?t=1604087386 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Kerbal Space Program</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">27 апр. 2015</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;94% из 67,692 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="69900">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        699 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/305620/The_Long_Dark/?snr=1_7_7_240_150_1"  data-ds-appid="305620" data-ds-itemkey="App_305620" data-ds-tagids="[1100689,1662,1695,3834,4166,3839,4182]" data-ds-crtrids="[33268311]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:305620,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/305620/capsule_sm_120_alt_assets_1.jpg?t=1608080968" srcset="https://steamcdn-a.akamaihd.net/steam/apps/305620/capsule_sm_120_alt_assets_1.jpg?t=1608080968 1x, https://steamcdn-a.akamaihd.net/steam/apps/305620/capsule_231x87_alt_assets_1.jpg?t=1608080968 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">The Long Dark</span>
                    <p>
                        <span class="platform_img win"></span><span class="platform_img mac"></span><span class="platform_img linux"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">1 авг. 2017</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;91% из 64,627 обзоров положительные.&lt;br&gt;&lt;br&gt;Замечены периоды обзоров не по теме. Учитывая ваши настройки, мы исключили эти обзоры из общего рейтинга.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="47500">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        475 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            		<a href="https://store.steampowered.com/app/617290/Remnant_From_the_Ashes/?snr=1_7_7_240_150_1"  data-ds-appid="617290" data-ds-itemkey="App_617290" data-ds-tagids="[29482,19,122,21,1685,3814,3859]" data-ds-descids="[2,5]" data-ds-crtrids="[32981301]" onmouseover="GameHover( this, event, 'global_hover', {&quot;type&quot;:&quot;app&quot;,&quot;id&quot;:617290,&quot;public&quot;:1,&quot;v6&quot;:1} );" onmouseout="HideGameHover( this, event, 'global_hover' )" class="search_result_row ds_collapse_flag " data-search-page="1" >
            <div class="col search_capsule"><img src="https://steamcdn-a.akamaihd.net/steam/apps/617290/capsule_sm_120.jpg?t=1605745130" srcset="https://steamcdn-a.akamaihd.net/steam/apps/617290/capsule_sm_120.jpg?t=1605745130 1x, https://steamcdn-a.akamaihd.net/steam/apps/617290/capsule_231x87.jpg?t=1605745130 2x"></div>
            <div class="responsive_search_name_combined">
                <div class="col search_name ellipsis">
                    <span class="title">Remnant: From the Ashes</span>
                    <p>
                        <span class="platform_img win"></span>                    </p>
                </div>
                <div class="col search_released responsive_secondrow">19 авг. 2019</div>
                <div class="col search_reviewscore responsive_secondrow">
                                            <span class="search_review_summary positive" data-tooltip-html="Очень положительные&lt;br&gt;84% из 28,899 обзоров положительные.">
								</span>
                                    </div>


                <div class="col search_price_discount_combined responsive_secondrow" data-price-final="129700">
                    <div class="col search_discount responsive_secondrow">
                        
                    </div>
                    <div class="col search_price  responsive_secondrow">
                        1297 pуб.                    </div>
                </div>
            </div>


            <div style="clear: left;"></div>
        </a>
            <!-- End List Items -->


    """
