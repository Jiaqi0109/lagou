import re

html = '''
                                              <span>后端开发</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/Java/" data-lg-tj-id="4O00" data-lg-tj-no="0101" data-lg-tj-cid="idnull" class="curr">Java</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/C%2B%2B/" data-lg-tj-id="4O00" data-lg-tj-no="0102" data-lg-tj-cid="idnull" class="curr">C++</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/PHP/" data-lg-tj-id="4O00" data-lg-tj-no="0103" data-lg-tj-cid="idnull" class="curr">PHP</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/shujuwajue/" data-lg-tj-id="4O00" data-lg-tj-no="0104" data-lg-tj-cid="idnull" class="curr">数据挖掘</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/sousuosuanfa/" data-lg-tj-id="4O00" data-lg-tj-no="0105" data-lg-tj-cid="idnull" class="">搜索算法</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/jingzhuntuijian/" data-lg-tj-id="4O00" data-lg-tj-no="0106" data-lg-tj-cid="idnull" class="">精准推荐</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/C/" data-lg-tj-id="4O00" data-lg-tj-no="0107" data-lg-tj-cid="idnull" class="">C</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/C%23/" data-lg-tj-id="4O00" data-lg-tj-no="0108" data-lg-tj-cid="idnull" class="">C#</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/quanzhangongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="0109" data-lg-tj-cid="idnull" class="">全栈工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/.NET/" data-lg-tj-id="4O00" data-lg-tj-no="0110" data-lg-tj-cid="idnull" class="">.NET</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/Hadoop/" data-lg-tj-id="4O00" data-lg-tj-no="0111" data-lg-tj-cid="idnull" class="">Hadoop</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/Python/" data-lg-tj-id="4O00" data-lg-tj-no="0112" data-lg-tj-cid="idnull" class="">Python</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/Delphi/" data-lg-tj-id="4O00" data-lg-tj-no="0113" data-lg-tj-cid="idnull" class="">Delphi</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/VB/" data-lg-tj-id="4O00" data-lg-tj-no="0114" data-lg-tj-cid="idnull" class="">VB</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/Perl/" data-lg-tj-id="4O00" data-lg-tj-no="0115" data-lg-tj-cid="idnull" class="">Perl</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/Ruby/" data-lg-tj-id="4O00" data-lg-tj-no="0116" data-lg-tj-cid="idnull" class="">Ruby</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/Node.js/" data-lg-tj-id="4O00" data-lg-tj-no="0117" data-lg-tj-cid="idnull" class="">Node.js</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/go/" data-lg-tj-id="4O00" data-lg-tj-no="0118" data-lg-tj-cid="idnull" class="">Go</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/asp/" data-lg-tj-id="4O00" data-lg-tj-no="0119" data-lg-tj-cid="idnull" class="">ASP</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/shell/" data-lg-tj-id="4O00" data-lg-tj-no="0120" data-lg-tj-cid="idnull" class="">Shell</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/qukuailian/" data-lg-tj-id="4O00" data-lg-tj-no="0121" data-lg-tj-cid="idnull" class="curr">区块链</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/houduankaifaqita/" data-lg-tj-id="4O00" data-lg-tj-no="0122" data-lg-tj-cid="idnull" class="">后端开发其它</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>移动开发</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/HTML5/" data-lg-tj-id="4O00" data-lg-tj-no="0201" data-lg-tj-cid="idnull" class="">HTML5</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/Android/" data-lg-tj-id="4O00" data-lg-tj-no="0202" data-lg-tj-cid="idnull" class="curr">Android</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/iOS/" data-lg-tj-id="4O00" data-lg-tj-no="0203" data-lg-tj-cid="idnull" class="curr">iOS</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/WP/" data-lg-tj-id="4O00" data-lg-tj-no="0204" data-lg-tj-cid="idnull" class="">WP</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/yidongkaifaqita/" data-lg-tj-id="4O00" data-lg-tj-no="0205" data-lg-tj-cid="idnull" class="">移动开发其它</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>前端开发</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/webqianduan/" data-lg-tj-id="4O00" data-lg-tj-no="0301" data-lg-tj-cid="idnull" class="">web前端</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/Flash/" data-lg-tj-id="4O00" data-lg-tj-no="0302" data-lg-tj-cid="idnull" class="">Flash</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/html51/" data-lg-tj-id="4O00" data-lg-tj-no="0303" data-lg-tj-cid="idnull" class="curr">html5</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/JavaScript/" data-lg-tj-id="4O00" data-lg-tj-no="0304" data-lg-tj-cid="idnull" class="">JavaScript</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/U3D/" data-lg-tj-id="4O00" data-lg-tj-no="0305" data-lg-tj-cid="idnull" class="">U3D</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/COCOS2D-X/" data-lg-tj-id="4O00" data-lg-tj-no="0306" data-lg-tj-cid="idnull" class="">COCOS2D-X</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/qianduankaifaqita/" data-lg-tj-id="4O00" data-lg-tj-no="0307" data-lg-tj-cid="idnull" class="">前端开发其它</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>人工智能<i class="icon_new"></i></span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/shenduxuexi/" data-lg-tj-id="4O00" data-lg-tj-no="0401" data-lg-tj-cid="idnull" class="curr">深度学习</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/jiqixuexi/" data-lg-tj-id="4O00" data-lg-tj-no="0402" data-lg-tj-cid="idnull" class="curr">机器学习</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/tuxiangchuli/" data-lg-tj-id="4O00" data-lg-tj-no="0403" data-lg-tj-cid="idnull" class="">图像处理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/tuxiangshibie/" data-lg-tj-id="4O00" data-lg-tj-no="0404" data-lg-tj-cid="idnull" class="">图像识别</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/yuyinshibie/" data-lg-tj-id="4O00" data-lg-tj-no="0405" data-lg-tj-cid="idnull" class="">语音识别</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/jiqishijue/" data-lg-tj-id="4O00" data-lg-tj-no="0406" data-lg-tj-cid="idnull" class="">机器视觉</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/suanfagongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="0407" data-lg-tj-cid="idnull" class="">算法工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/ziranyuyanchuli/" data-lg-tj-id="4O00" data-lg-tj-no="0408" data-lg-tj-cid="idnull" class="curr">自然语言处理</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>测试</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/ceshigongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="0501" data-lg-tj-cid="idnull" class="">测试工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/zidonghuaceshi/" data-lg-tj-id="4O00" data-lg-tj-no="0502" data-lg-tj-cid="idnull" class="">自动化测试</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/gongnengceshi/" data-lg-tj-id="4O00" data-lg-tj-no="0503" data-lg-tj-cid="idnull" class="">功能测试</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/xingnengceshi/" data-lg-tj-id="4O00" data-lg-tj-no="0504" data-lg-tj-cid="idnull" class="">性能测试</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/ceshikaifa/" data-lg-tj-id="4O00" data-lg-tj-no="0505" data-lg-tj-cid="idnull" class="">测试开发</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/youxiceshi/" data-lg-tj-id="4O00" data-lg-tj-no="0506" data-lg-tj-cid="idnull" class="">游戏测试</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/baiheceshi/" data-lg-tj-id="4O00" data-lg-tj-no="0507" data-lg-tj-cid="idnull" class="">白盒测试</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/huiheceshi/" data-lg-tj-id="4O00" data-lg-tj-no="0508" data-lg-tj-cid="idnull" class="">灰盒测试</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/heiheceshi/" data-lg-tj-id="4O00" data-lg-tj-no="0509" data-lg-tj-cid="idnull" class="">黑盒测试</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/shoujiceshi/" data-lg-tj-id="4O00" data-lg-tj-no="0510" data-lg-tj-cid="idnull" class="">手机测试</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/yingjianceshi/" data-lg-tj-id="4O00" data-lg-tj-no="0511" data-lg-tj-cid="idnull" class="">硬件测试</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/ceshijingli2/" data-lg-tj-id="4O00" data-lg-tj-no="0512" data-lg-tj-cid="idnull" class="">测试经理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/ceshiqita/" data-lg-tj-id="4O00" data-lg-tj-no="0513" data-lg-tj-cid="idnull" class="">测试其它</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>运维</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/yunweigongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="0601" data-lg-tj-cid="idnull" class="">运维工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/yunweikaifagongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="0602" data-lg-tj-cid="idnull" class="">运维开发工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/wangluogongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="0603" data-lg-tj-cid="idnull" class="">网络工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/xitonggongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="0604" data-lg-tj-cid="idnull" class="">系统工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/ITzhichi/" data-lg-tj-id="4O00" data-lg-tj-no="0605" data-lg-tj-cid="idnull" class="">IT支持</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/idc/" data-lg-tj-id="4O00" data-lg-tj-no="0606" data-lg-tj-cid="idnull" class="">IDC</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/cdn/" data-lg-tj-id="4O00" data-lg-tj-no="0607" data-lg-tj-cid="idnull" class="">CDN</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/f5/" data-lg-tj-id="4O00" data-lg-tj-no="0608" data-lg-tj-cid="idnull" class="">F5</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/xitongguanliyuan/" data-lg-tj-id="4O00" data-lg-tj-no="0609" data-lg-tj-cid="idnull" class="">系统管理员</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/bingdufenxi/" data-lg-tj-id="4O00" data-lg-tj-no="0610" data-lg-tj-cid="idnull" class="">病毒分析</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/webanquan/" data-lg-tj-id="4O00" data-lg-tj-no="0611" data-lg-tj-cid="idnull" class="">WEB安全</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/wangluoanquan/" data-lg-tj-id="4O00" data-lg-tj-no="0612" data-lg-tj-cid="idnull" class="">网络安全</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/xitonganquan/" data-lg-tj-id="4O00" data-lg-tj-no="0613" data-lg-tj-cid="idnull" class="">系统安全</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/yunweijingli/" data-lg-tj-id="4O00" data-lg-tj-no="0614" data-lg-tj-cid="idnull" class="">运维经理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/yunweiqita/" data-lg-tj-id="4O00" data-lg-tj-no="0615" data-lg-tj-cid="idnull" class="">运维其它</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>DBA</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/MySQL/" data-lg-tj-id="4O00" data-lg-tj-no="0701" data-lg-tj-cid="idnull" class="">MySQL</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/SQLServer/" data-lg-tj-id="4O00" data-lg-tj-no="0702" data-lg-tj-cid="idnull" class="">SQLServer</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/Oracle/" data-lg-tj-id="4O00" data-lg-tj-no="0703" data-lg-tj-cid="idnull" class="">Oracle</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/DB2/" data-lg-tj-id="4O00" data-lg-tj-no="0704" data-lg-tj-cid="idnull" class="">DB2</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/MongoDB/" data-lg-tj-id="4O00" data-lg-tj-no="0705" data-lg-tj-cid="idnull" class="">MongoDB</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/etl/" data-lg-tj-id="4O00" data-lg-tj-no="0706" data-lg-tj-cid="idnull" class="">ETL</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/hive/" data-lg-tj-id="4O00" data-lg-tj-no="0707" data-lg-tj-cid="idnull" class="">Hive</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/shujucangku/" data-lg-tj-id="4O00" data-lg-tj-no="0708" data-lg-tj-cid="idnull" class="">数据仓库</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/dbaqita/" data-lg-tj-id="4O00" data-lg-tj-no="0709" data-lg-tj-cid="idnull" class="">DBA其它</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                


                                                <span>高端职位</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/jishujingli/" data-lg-tj-id="4O00" data-lg-tj-no="0801" data-lg-tj-cid="idnull" class="">技术经理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/jishuzongjian/" data-lg-tj-id="4O00" data-lg-tj-no="0802" data-lg-tj-cid="idnull" class="curr">技术总监</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/jiagoushi/" data-lg-tj-id="4O00" data-lg-tj-no="0803" data-lg-tj-cid="idnull" class="curr">架构师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/CTO/" data-lg-tj-id="4O00" data-lg-tj-no="0804" data-lg-tj-cid="idnull" class="curr">CTO</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/yunweizongjian/" data-lg-tj-id="4O00" data-lg-tj-no="0805" data-lg-tj-cid="idnull" class="">运维总监</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/jishuhehuoren/" data-lg-tj-id="4O00" data-lg-tj-no="0806" data-lg-tj-cid="idnull" class="">技术合伙人</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/xiangmuzongjian/" data-lg-tj-id="4O00" data-lg-tj-no="0807" data-lg-tj-cid="idnull" class="">项目总监</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/ceshizongjian/" data-lg-tj-id="4O00" data-lg-tj-no="0808" data-lg-tj-cid="idnull" class="">测试总监</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/anquanzhuanjia/" data-lg-tj-id="4O00" data-lg-tj-no="0809" data-lg-tj-cid="idnull" class="">安全专家</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/gaoduanjishuzhiweiqita/" data-lg-tj-id="4O00" data-lg-tj-no="0810" data-lg-tj-cid="idnull" class="">高端技术职位其它</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>项目管理</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/xiangmujingli/" data-lg-tj-id="4O00" data-lg-tj-no="0901" data-lg-tj-cid="idnull" class="">项目经理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/xiangmuzhuli/" data-lg-tj-id="4O00" data-lg-tj-no="0902" data-lg-tj-cid="idnull" class="">项目助理</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>硬件开发</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/yingjian/" data-lg-tj-id="4O00" data-lg-tj-no="1001" data-lg-tj-cid="idnull" class="">硬件</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/qianrushi/" data-lg-tj-id="4O00" data-lg-tj-no="1002" data-lg-tj-cid="idnull" class="">嵌入式</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/zidonghua/" data-lg-tj-id="4O00" data-lg-tj-no="1003" data-lg-tj-cid="idnull" class="">自动化</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/danpianji/" data-lg-tj-id="4O00" data-lg-tj-no="1004" data-lg-tj-cid="idnull" class="">单片机</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/dianlusheji/" data-lg-tj-id="4O00" data-lg-tj-no="1005" data-lg-tj-cid="idnull" class="">电路设计</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/qudongkaifa/" data-lg-tj-id="4O00" data-lg-tj-no="1006" data-lg-tj-cid="idnull" class="">驱动开发</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/xitongjicheng/" data-lg-tj-id="4O00" data-lg-tj-no="1007" data-lg-tj-cid="idnull" class="">系统集成</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/fpgakaifa/" data-lg-tj-id="4O00" data-lg-tj-no="1008" data-lg-tj-cid="idnull" class="">FPGA开发</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/dspkaifa/" data-lg-tj-id="4O00" data-lg-tj-no="1009" data-lg-tj-cid="idnull" class="">DSP开发</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/armkaifa/" data-lg-tj-id="4O00" data-lg-tj-no="1010" data-lg-tj-cid="idnull" class="">ARM开发</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/pcbgongyi/" data-lg-tj-id="4O00" data-lg-tj-no="1011" data-lg-tj-cid="idnull" class="">PCB工艺</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/mujusheji/" data-lg-tj-id="4O00" data-lg-tj-no="1012" data-lg-tj-cid="idnull" class="">模具设计</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/rechuandao/" data-lg-tj-id="4O00" data-lg-tj-no="1013" data-lg-tj-cid="idnull" class="">热传导</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/cailiaogongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="1014" data-lg-tj-cid="idnull" class="">材料工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/jingyigongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="1015" data-lg-tj-cid="idnull" class="">精益工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/shepingongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="1016" data-lg-tj-cid="idnull" class="">射频工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/yingjiankaifaqita/" data-lg-tj-id="4O00" data-lg-tj-no="1017" data-lg-tj-cid="idnull" class="">硬件开发其它</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>企业软件</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/shishigongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="1101" data-lg-tj-cid="idnull" class="">实施工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/shouqiangongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="1102" data-lg-tj-cid="idnull" class="">售前工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/shouhougongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="1103" data-lg-tj-cid="idnull" class="">售后工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/bigongchengshi/" data-lg-tj-id="4O00" data-lg-tj-no="1104" data-lg-tj-cid="idnull" class="">BI工程师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        <a href="https://www.lagou.com/zhaopin/qiyeruanjianqita/" data-lg-tj-id="4O00" data-lg-tj-no="1105" data-lg-tj-cid="idnull" class="">企业软件其它</a>

                                            </dd>
                </dl>
                            </div>
        </div>
                <div class="menu_box">
            <div class="menu_main job_hopping">
                <div class="category-list">
                    <h2>
                        产品
                        

                    </h2>

                    
                    
                                                
                                                
                    <a href="https://www.lagou.com/zhaopin/chanpinzongjian/" data-lg-tj-id="4B00" data-lg-tj-no="0001" data-lg-tj-cid="idnull">产品总监</a>
                    
                                                
                                                
                    <a href="https://www.lagou.com/zhaopin/chanpinjingli1/" data-lg-tj-id="4B00" data-lg-tj-no="0002" data-lg-tj-cid="idnull">产品经理</a>
                    
                                                
                                                
                    <a href="https://www.lagou.com/zhaopin/shujuchanpinjingli/" data-lg-tj-id="4B00" data-lg-tj-no="0003" data-lg-tj-cid="idnull">数据产品经理</a>
                    
                                                
                                                
                    <a href="https://www.lagou.com/zhaopin/youxicehua/" data-lg-tj-id="4B00" data-lg-tj-no="0004" data-lg-tj-cid="idnull">游戏策划</a>
                                        <i class="arrow"></i>
                </div>
            </div>
            <div class="menu_sub dn">
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>产品经理</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/chanpinjingli1/" data-lg-tj-id="4P00" data-lg-tj-no="0101" data-lg-tj-cid="idnull" class="curr">产品经理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/wangyechanpinjingli/" data-lg-tj-id="4P00" data-lg-tj-no="0102" data-lg-tj-cid="idnull" class="">网页产品经理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/yidongchanpinjingli/" data-lg-tj-id="4P00" data-lg-tj-no="0103" data-lg-tj-cid="idnull" class="">移动产品经理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/chanpinzhuli/" data-lg-tj-id="4P00" data-lg-tj-no="0104" data-lg-tj-cid="idnull" class="">产品助理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/shujuchanpinjingli/" data-lg-tj-id="4P00" data-lg-tj-no="0105" data-lg-tj-cid="idnull" class="curr">数据产品经理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/dianshangchanpinjingli/" data-lg-tj-id="4P00" data-lg-tj-no="0106" data-lg-tj-cid="idnull" class="">电商产品经理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/youxicehua/" data-lg-tj-id="4P00" data-lg-tj-no="0107" data-lg-tj-cid="idnull" class="curr">游戏策划</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/chanpinshixisheng/" data-lg-tj-id="4P00" data-lg-tj-no="0108" data-lg-tj-cid="idnull" class="">产品实习生</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>产品设计师</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/wangyechanpinshejishi/" data-lg-tj-id="4P00" data-lg-tj-no="0201" data-lg-tj-cid="idnull" class="">网页产品设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/wuxianchanpinshejishi/" data-lg-tj-id="4P00" data-lg-tj-no="0202" data-lg-tj-cid="idnull" class="">无线产品设计师</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                


                                                <span>高端职位</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/chanpinbujingli/" data-lg-tj-id="4P00" data-lg-tj-no="0301" data-lg-tj-cid="idnull" class="">产品部经理</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/chanpinzongjian/" data-lg-tj-id="4P00" data-lg-tj-no="0302" data-lg-tj-cid="idnull" class="curr">产品总监</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                    <a href="https://www.lagou.com/zhaopin/youxizhizuoren/" data-lg-tj-id="4P00" data-lg-tj-no="0303" data-lg-tj-cid="idnull" class="">游戏制作人</a>

                                            </dd>
                </dl>
                            </div>
        </div>
                <div class="menu_box">
            <div class="menu_main job_hopping">
                <div class="category-list">
                    <h2>
                        设计
                        

                    </h2>

                    
                    
                                                
                                                
                    <a href="https://www.lagou.com/zhaopin/UIshejishi/" data-lg-tj-id="4C00" data-lg-tj-no="0001" data-lg-tj-cid="idnull">UI设计师</a>
                    
                                                
                                                
                    <a href="https://www.lagou.com/zhaopin/jiaohusheji/" data-lg-tj-id="4C00" data-lg-tj-no="0002" data-lg-tj-cid="idnull">交互设计</a>
                    
                                                
                                                
                    <a href="https://www.lagou.com/zhaopin/wangyeshejishi/" data-lg-tj-id="4C00" data-lg-tj-no="0003" data-lg-tj-cid="idnull">网页设计师</a>
                    
                                                
                                                
                    <a href="https://www.lagou.com/zhaopin/pingmianshejishi/" data-lg-tj-id="4C00" data-lg-tj-no="0004" data-lg-tj-cid="idnull">平面设计师</a>
                    
                                                
                                                
                    <a href="https://www.lagou.com/zhaopin/shijueshejishi/" data-lg-tj-id="4C00" data-lg-tj-no="0005" data-lg-tj-cid="idnull">视觉设计师</a>
                                        <i class="arrow"></i>
                </div>
            </div>
            <div class="menu_sub dn">
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>视觉设计</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/shijueshejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0101" data-lg-tj-cid="idnull" class="curr">视觉设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/wangyeshejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0102" data-lg-tj-cid="idnull" class="curr">网页设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/Flashshejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0103" data-lg-tj-cid="idnull" class="">Flash设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/APPshejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0104" data-lg-tj-cid="idnull" class="">APP设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/UIshejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0105" data-lg-tj-cid="idnull" class="curr">UI设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/pingmianshejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0106" data-lg-tj-cid="idnull" class="curr">平面设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/meishushejishi%EF%BC%882D3D%EF%BC%89/" data-lg-tj-id="4Q00" data-lg-tj-no="0107" data-lg-tj-cid="idnull" class="">美术设计师（2D/3D）</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/guanggaoshejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0108" data-lg-tj-cid="idnull" class="">广告设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/duomeitishejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0109" data-lg-tj-cid="idnull" class="">多媒体设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/yuanhuashi/" data-lg-tj-id="4Q00" data-lg-tj-no="0110" data-lg-tj-cid="idnull" class="">原画师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/youxitexiao/" data-lg-tj-id="4Q00" data-lg-tj-no="0111" data-lg-tj-cid="idnull" class="">游戏特效</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/youxijiemianshejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0112" data-lg-tj-cid="idnull" class="">游戏界面设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/youxichangjing/" data-lg-tj-id="4Q00" data-lg-tj-no="0113" data-lg-tj-cid="idnull" class="">游戏场景</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/youxijiaose/" data-lg-tj-id="4Q00" data-lg-tj-no="0114" data-lg-tj-cid="idnull" class="">游戏角色</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/youxidongzuo/" data-lg-tj-id="4Q00" data-lg-tj-no="0115" data-lg-tj-cid="idnull" class="">游戏动作</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>交互设计</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/jiaohushejishi1/" data-lg-tj-id="4Q00" data-lg-tj-no="0201" data-lg-tj-cid="idnull" class="">交互设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/wuxianjiaohushejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0202" data-lg-tj-cid="idnull" class="">无线交互设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/wangyejiaohushejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0203" data-lg-tj-cid="idnull" class="">网页交互设计师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/yingjianjiaohushejishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0204" data-lg-tj-cid="idnull" class="">硬件交互设计师</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                    


                                                <span>用户研究</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/shujufenxishi/" data-lg-tj-id="4Q00" data-lg-tj-no="0301" data-lg-tj-cid="idnull" class="">数据分析师</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/yonghuyanjiuyuan/" data-lg-tj-id="4Q00" data-lg-tj-no="0302" data-lg-tj-cid="idnull" class="">用户研究员</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/youxishuzhicehua/" data-lg-tj-id="4Q00" data-lg-tj-no="0303" data-lg-tj-cid="idnull" class="">游戏数值策划</a>

                                            </dd>
                </dl>
                                <dl>
                                        <dt>
                                                
                                                
                                                                                                                                                                                                                                                                                                                                                                                                                                


                                                <span>高端职位</span>
                    </dt>
                    <dd>
                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/shejijinglizhuguan/" data-lg-tj-id="4Q00" data-lg-tj-no="0401" data-lg-tj-cid="idnull" class="">设计经理/主管</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/shejizongjian/" data-lg-tj-id="4Q00" data-lg-tj-no="0402" data-lg-tj-cid="idnull" class="">设计总监</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/shijueshejijinglizhuguan/" data-lg-tj-id="4Q00" data-lg-tj-no="0403" data-lg-tj-cid="idnull" class="">视觉设计经理/主管</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/shijueshejizongjian/" data-lg-tj-id="4Q00" data-lg-tj-no="0404" data-lg-tj-cid="idnull" class="">视觉设计总监</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/jiaohushejijinglizhuguan/" data-lg-tj-id="4Q00" data-lg-tj-no="0405" data-lg-tj-cid="idnull" class="">交互设计经理/主管</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/jiaohushejizongjian/" data-lg-tj-id="4Q00" data-lg-tj-no="0406" data-lg-tj-cid="idnull" class="">交互设计总监</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/yonghuyanjiujinglizhuguan/" data-lg-tj-id="4Q00" data-lg-tj-no="0407" data-lg-tj-cid="idnull" class="">用户研究经理/主管</a>

                        
                                                        
                                                        
                                                                                                                                                                                                                                                                                                                                                                                                <a href="https://www.lagou.com/zhaopin/yonghuyanjiuzongjian/" data-lg-tj-id="4Q00" data-lg-tj-no="0408" data-lg-tj-cid="idnull" class="">用户研究总监</a>
'''

span = re.compile('">(.*?)</a>')

data = span.findall(html)

with open('./KEYWORDS/category.txt', 'w') as f:
    for d in data:
        f.write(d+'\n')


'''
Java
C++
PHP
数据挖掘
搜索算法
精准推荐
C
C#
全栈工程师
.NET
Hadoop
Python
Delphi
VB
Perl
Ruby
Node.js
Go
ASP
Shell
区块链
后端开发其它
HTML5
Android
iOS
WP
移动开发其它
web前端
Flash
html5
JavaScript
U3D
COCOS2D-X
前端开发其它
深度学习
机器学习
图像处理
图像识别
语音识别
机器视觉
算法工程师
自然语言处理
测试工程师
自动化测试
功能测试
性能测试
测试开发
游戏测试
白盒测试
灰盒测试
黑盒测试
手机测试
硬件测试
测试经理
测试其它
运维工程师
运维开发工程师
网络工程师
系统工程师
IT支持
IDC
CDN
F5
系统管理员
病毒分析
WEB安全
网络安全
系统安全
运维经理
运维其它
MySQL
SQLServer
Oracle
DB2
MongoDB
ETL
Hive
数据仓库
DBA其它
技术经理
技术总监
架构师
CTO
运维总监
技术合伙人
项目总监
测试总监
安全专家
高端技术职位其它
项目经理
项目助理
硬件
嵌入式
自动化
单片机
电路设计
驱动开发
系统集成
FPGA开发
DSP开发
ARM开发
PCB工艺
模具设计
热传导
材料工程师
精益工程师
射频工程师
硬件开发其它
实施工程师
售前工程师
售后工程师
BI工程师
企业软件其它
产品总监
产品经理
数据产品经理
游戏策划
产品经理
网页产品经理
移动产品经理
产品助理
数据产品经理
电商产品经理
游戏策划
产品实习生
网页产品设计师
无线产品设计师
产品部经理
产品总监
游戏制作人
UI设计师
交互设计
网页设计师
平面设计师
视觉设计师
视觉设计师
网页设计师
Flash设计师
APP设计师
UI设计师
平面设计师
美术设计师（2D/3D）
广告设计师
多媒体设计师
原画师
游戏特效
游戏界面设计师
游戏场景
游戏角色
游戏动作
交互设计师
无线交互设计师
网页交互设计师
硬件交互设计师
数据分析师
用户研究员
游戏数值策划
设计经理/主管
设计总监
视觉设计经理/主管
视觉设计总监
交互设计经理/主管
交互设计总监
用户研究经理/主管
用户研究总监
新媒体运营
编辑
数据运营
运营总监
COO
用户运营
产品运营
数据运营
内容运营
活动运营
商家运营
品类运营
游戏运营
网络推广
运营专员
网店运营
新媒体运营
海外运营
运营经理
副主编
内容编辑
文案策划
记者
售前咨询
售后客服
淘宝客服
客服经理
主编
运营总监
COO
客服总监
市场推广
市场总监
市场策划
BD
销售总监
销售经理
市场营销
市场策划
市场顾问
市场推广
SEO
SEM
商务渠道
商业数据分析
活动策划
网络营销
海外市场
政府关系
媒介经理
广告协调
品牌公关
销售专员
销售经理
客户代表
大客户代表
BD经理
商务渠道
渠道销售
代理商销售
销售助理
电话销售
销售顾问
商品经理
物流
仓储
采购专员
采购经理
商品经理
分析师
投资顾问
投资经理
市场总监
销售总监
商务总监
CMO
公关总监
采购总监
投资总监
HR
行政
财务
审计
人力资源
招聘
HRBP
人事/HR
培训经理
薪资福利经理
绩效考核经理
员工关系
助理
前台
行政
总助
文秘
会计
出纳
财务
结算
税务
审计
风控
法务
律师
专利
行政总监/经理
财务总监/经理
HRD/HRM
CFO
CEO
投资
融资
并购
风控
投资经理
分析师
投资助理
融资
并购
行业研究
投资者关系
资产管理
理财顾问
交易员
风控
资信评估
合规稽查
律师
审计
法务
会计
清算
投资总监
融资总监
并购总监
风控总监
副总裁
'''
