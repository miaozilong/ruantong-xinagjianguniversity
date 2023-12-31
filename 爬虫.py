from tools.support import greet
from loguru import logger as log
# 导入 requests 包
import requests
from bs4 import BeautifulSoup
import os

log.add('file_{time:YYYY-MM-DD}.log', format="{name} {level} {message}", level="TRACE", rotation='5 MB',
        encoding='utf-8')

if __name__ == "__main__":
    cookies = {
        '_lxsdk_cuid': '188d129013cc8-0953e4c6d31555-26031d51-1fa400-188d129013cc8',
        '_lxsdk': '188d129013cc8-0953e4c6d31555-26031d51-1fa400-188d129013cc8',
        'uuid': '188d129013cc8-0953e4c6d31555-26031d51-1fa400-188d129013cc8',
        '_lx_utm': 'utm_source%3Dgoogle%26utm_medium%3Dorganic',
        '_lxsdk_s': '188db6471d6-3c-3af-ef%7C%7C17',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': '_lxsdk_cuid=188d129013cc8-0953e4c6d31555-26031d51-1fa400-188d129013cc8; _lxsdk=188d129013cc8-0953e4c6d31555-26031d51-1fa400-188d129013cc8; uuid=188d129013cc8-0953e4c6d31555-26031d51-1fa400-188d129013cc8; _lx_utm=utm_source%3Dgoogle%26utm_medium%3Dorganic; _lxsdk_s=188db6471d6-3c-3af-ef%7C%7C17',
        'Referer': 'https://piaofang.maoyan.com/rankings/year',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    url = 'https://piaofang.maoyan.com/rankings/year'
    res = requests.get(url, cookies=cookies, headers=headers)
    res.encoding = res.apparent_encoding
    # 返回网页内容
    # log.debug(res.text)

    rsptext = """
    <!DOCTYPE html>
<html class="">
<head>
<meta charset="utf-8" />
<meta name="keywords" content="猫眼票房分析,猫眼电影,电影票房,实时票房,日票房,预售票房,影片票房趋势,受众画像,实时排片,预售排片,上座率,历史票房" />
<meta name="description" content="猫眼票房分析，提供准确的每日电影实时票房、排片、上座率查询，为电影从业者提供及时、专业的数据分析服务" />
<meta http-equiv="Cache-Control" CONTENT="no-cache" />
<meta http-equiv="Content-Security-Policy" content="default-src js://* wx.qlogo.cn thirdwx.qlogo.cn *.tanx.com *.mmstat.com *.meituan.com passport.st.maoyan.team verify.maoyan.com www.dpfile.com *.sankuai.com *.wandafilm.com https://i.meituan.com/ https://m.dianping.com/ https://ebsnew.boc.cn https://ms0.meituan.com https://mc0.meituan.com https://mpay.meituan.com https://npay.meituan.com 192.168.4.223:9999 *.maoyan.com https://*.meituan.com https://*.sankuai.com https://*.meituan.net http://*.meituan.net www.google-analytics.com wvjbscheme://* imeituan://* *.dianping.com *.dpfile.com *.51ping.com mymonitor.movie.dev.sankuai.com http://res.wx.qq.com https://res.wx.qq.com open.weixin.qq.com ytscheme://* alipaybridge://* alipaymonitor://* pub.idqqimg.com *.qianbao.qq.com *.qq.com c.mipcdn.com *.baidu.com wx.tenpay.com *.gtimg.cn validate-ocean.sankuai.com open.95516.com *.pipi.cn https://*.cos.ap-beijing.myqcloud.com jsbridge://* 'self' 'unsafe-inline' 'unsafe-eval' mqqapi://* blob: gap: data:;" />
<meta http-equiv="Pragma" CONTENT="no-cache" />
<meta http-equiv="cache-control" CONTENT="no-store" />
<meta name="format-detection" content="telephone=no" />
<meta name="csrf" content="c0b3daad6db9a5032e8d56f8aff23069bec999ce" />
<meta name="theme-color" content="#F1303D">
<!-- 上报通道标识 -->
<meta name="lx:category" content="moviepro">
<!-- 上报应用标识 -->
<meta name="lx:appnm" content="moviepro_i">
<!-- 页面名称：i版_专业服务_影人详情页，上报页面标识 -->
<meta name="lx:cid" content="影片总票房排行榜页">
<link rel="dns-prefetch" href="//analytics.meituan.com" />
<link rel="dns-prefetch" href="//analytics.meituan.net"/>
<link rel="dns-prefetch" href="//wreport.meituan.net"/>
<link rel="dns-prefetch" href="//report.meituan.net"/>
<link rel="dns-prefetch" href="//ms0.meituan.net" />
<link rel="dns-prefetch" href="//mc.meituan.net" />
<link rel="dns-prefetch" href="//s0.meituan.net" />
<link rel="dns-prefetch" href="//p0.meituan.net" />
<link rel="dns-prefetch" href="//p1.meituan.net" />
<link rel="apple-touch-icon" href="//obj.pipi.cn/festatic/moviepro/img/wx_pic-daf3a7c4.png" />
<link rel="icon" type="image/x-icon" href="//obj.pipi.cn/festatic/moviepro/img/favicon-f8defb48.ico" />
<meta name="viewport" content="initial-scale=1, width=device-width, maximum-scale=1, user-scalable=no, viewport-fit=cover">
<link rel="shortcut icon" type="image/x-icon" href="//obj.pipi.cn/festatic/moviepro/img/favicon-f8defb48.ico" />
<script>
    "use strict";!function(u,d){var t="owl",e="_Owl_",n="Owl",r="start",c="error",p="on"+c,f=u[p],h="addEventListener",l="attachEvent",v="isReady",b="dataSet";u[t]=u[t]||function(){try{u[t].q=u[t].q||[];var e=[].slice.call(arguments);e[0]===r?u[n]&&u[n][r]?u[n][r](e[1]):u[t].q.unshift(e):u[t].q.push(e)}catch(e){}},u[e]=u[e]||{preTasks:[],pageData:[],use:function(e,t){this[v]?u[n][e](t):this.preTasks.push({api:e,data:[t]})},run:function(t){if(!(t=this).runned){t.runned=!0,t[b]=[],u[p]=function(){t[v]||t[b].push({type:"jsError",data:arguments}),f&&f.apply(u,arguments)},u[h]&&u[h]("unhandledrejection",function(e){t[v]||t[b].push({type:"jsError",data:[e]})});var e=function(e){!t[v]&&e&&t[b].push({type:"resError",data:[e]})};u[h]?u[h](c,e,!0):u[l]&&u[l](p,e);var n="MutationObserver",r=u[n]||u["WebKit"+n]||u["Moz"+n],a=u.performance||u.WebKitPerformance,s="disableMutaObserver";if(r&&a&&a.now)try{var i=-1,o=u.navigator.userAgent;-1<o.indexOf("compatible")&&-1<o.indexOf("MSIE")?(new RegExp("MSIE (\\d+\\.\\d+);").test(o),i=parseFloat(RegExp.$1)):-1<o.indexOf("Trident")&&-1<o.indexOf("rv:11.0")&&(i=11),-1!==i&&i<=11?t[s]=!0:(t.observer=new r(function(e){t.pageData.push({mutations:e,startTime:a.now()})})).observe(d,{childList:!0,subtree:!0})}catch(e){}else t[s]=!0}}},u[e].runned||u[e].run()}(window,document);
</script>
<script type="text/javascript">
document.addEventListener('DOMContentLoaded', function() {
    var images = document.querySelectorAll('.need-handle-pic');
    for(var i = 0; i < images.length; i++) {
        var imgItem = images[i];
        var className = imgItem.className;
        var src = imgItem.getAttribute('src');
        if (!src) {
            imgItem.className = className + ' has-no-pic';
            imgItem.setAttribute('alt', '');
        } else {
            imgItem.onerror = function(e) {
                e.target.className = className + ' has-error-pic';
                e.target.setAttribute('alt', '');
            }
        }
    }
});
</script>
<link rel="stylesheet" type="text/css" href="//obj.pipi.cn/festatic/moviepro/css/ranking-7f7b4db9.css" />
<title>影片总票房排行榜</title>
</head>
<body style="padding-top:1.84rem" data-index="0">
<div id="wx_pic" style="display:none;">
    <img src="//obj.pipi.cn/festatic/moviepro/img/wx_pic-daf3a7c4.png"/>
</div>
<header class="navBar ">
	<div class="nav-wrap-left">
		<a id="rank-back" class="back" data-com="hisBack">
			<i class="text-icon icon-back"></i>
		</a>
	</div>
    <h1 class="nav-header navBarTitle" style="margin-top:.16rem;"><img id="rank-logo" style="height:.6rem" src="
            //obj.pipi.cn/festatic/moviepro/img/logo_150717-febb7f98.png
    " /></h1>
</header>
<div class="select-year " id="tab-year">
    <ul>
        <li data-com="canTouch"  class="active" >全部</li>
        <li data-com="canTouch" >2023年</li>
        <li data-com="canTouch" >2022年</li>
        <li data-com="canTouch" >2021年</li>
        <li data-com="canTouch" >2020年</li>
        <li data-com="canTouch" >2019年</li>
        <li data-com="canTouch" >2018年</li>
        <li data-com="canTouch" >2017年</li>
        <li data-com="canTouch" >2016年</li>
        <li data-com="canTouch" >2015年</li>
        <li data-com="canTouch" >2014年</li>
        <li data-com="canTouch" >2013年</li>
        <li data-com="canTouch" >2012年</li>
        <li data-com="canTouch" >2011年</li>
    </ul>
</div>
<div id="total-box">
    <span id="year-box">中国电影票房总榜</span>
    <span id="update-time">(截至2023年6月21日)</span>
</div>
<div id="ranks-title">
    <ul class="row">
        <li class="col0">排名</li>
        <li class="col1">片名</li>
        <li class="col2 tr">票房(万元)</li>
        <li class="col3 tr">平均票价</li>
        <li class="col4 tr">场均人次</li>
    </ul>
</div>
<div id="ranks-list">
    <ul class="row" data-com="hrefTo,href:'/movie/257706'">
        <li class="col0">1</li>
        <li class="col1">
            <p class="first-line">长津湖</p>
            <p class="second-line">2021-09-30 上映</p>
        </li>
        <li class="col2 tr">577534</li>
        <li class="col3 tr">46.383896</li>
        <li class="col4 tr">22</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/344264'">
        <li class="col0">2</li>
        <li class="col1">
            <p class="first-line">战狼2</p>
            <p class="second-line">2017-07-27 上映</p>
        </li>
        <li class="col2 tr">569454</li>
        <li class="col3 tr">35.594273</li>
        <li class="col4 tr">37</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1299372'">
        <li class="col0">3</li>
        <li class="col1">
            <p class="first-line">你好，李焕英</p>
            <p class="second-line">2021-02-12 上映</p>
        </li>
        <li class="col2 tr">541308</li>
        <li class="col3 tr">44.756912</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1211270'">
        <li class="col0">4</li>
        <li class="col1">
            <p class="first-line">哪吒之魔童降世</p>
            <p class="second-line">2019-07-26 上映</p>
        </li>
        <li class="col2 tr">503570</li>
        <li class="col3 tr">35.692467</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248906'">
        <li class="col0">5</li>
        <li class="col1">
            <p class="first-line">流浪地球</p>
            <p class="second-line">2019-02-05 上映</p>
        </li>
        <li class="col2 tr">468736</li>
        <li class="col3 tr">44.59698</li>
        <li class="col4 tr">29</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1462626'">
        <li class="col0">6</li>
        <li class="col1">
            <p class="first-line">满江红</p>
            <p class="second-line">2023-01-22 上映</p>
        </li>
        <li class="col2 tr">454443</li>
        <li class="col3 tr">49.514133</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1217023'">
        <li class="col0">7</li>
        <li class="col1">
            <p class="first-line">唐人街探案3</p>
            <p class="second-line">2021-02-12 上映</p>
        </li>
        <li class="col2 tr">452341</li>
        <li class="col3 tr">47.60313</li>
        <li class="col4 tr">29</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248172'">
        <li class="col0">8</li>
        <li class="col1">
            <p class="first-line">复仇者联盟4：终局之战</p>
            <p class="second-line">2019-04-24 上映</p>
        </li>
        <li class="col2 tr">425013</li>
        <li class="col3 tr">48.958096</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1446115'">
        <li class="col0">9</li>
        <li class="col1">
            <p class="first-line">长津湖之水门桥</p>
            <p class="second-line">2022-02-01 上映</p>
        </li>
        <li class="col2 tr">406733</li>
        <li class="col3 tr">49.28735</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1366696'">
        <li class="col0">10</li>
        <li class="col1">
            <p class="first-line">流浪地球2</p>
            <p class="second-line">2023-01-22 上映</p>
        </li>
        <li class="col2 tr">402906</li>
        <li class="col3 tr">50.792725</li>
        <li class="col4 tr">21</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1182552'">
        <li class="col0">11</li>
        <li class="col1">
            <p class="first-line">红海行动</p>
            <p class="second-line">2018-02-16 上映</p>
        </li>
        <li class="col2 tr">365228</li>
        <li class="col3 tr">39.275932</li>
        <li class="col4 tr">32</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/344990'">
        <li class="col0">12</li>
        <li class="col1">
            <p class="first-line">唐人街探案2</p>
            <p class="second-line">2018-02-16 上映</p>
        </li>
        <li class="col2 tr">339777</li>
        <li class="col3 tr">38.757156</li>
        <li class="col4 tr">38</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246063'">
        <li class="col0">13</li>
        <li class="col1">
            <p class="first-line">美人鱼</p>
            <p class="second-line">2016-02-08 上映</p>
        </li>
        <li class="col2 tr">339120</li>
        <li class="col3 tr">36.668804</li>
        <li class="col4 tr">43</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1277939'">
        <li class="col0">14</li>
        <li class="col1">
            <p class="first-line">我和我的祖国</p>
            <p class="second-line">2019-09-30 上映</p>
        </li>
        <li class="col2 tr">317003</li>
        <li class="col3 tr">38.10905</li>
        <li class="col4 tr">35</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/346210'">
        <li class="col0">15</li>
        <li class="col1">
            <p class="first-line">八佰</p>
            <p class="second-line">2020-08-21 上映</p>
        </li>
        <li class="col2 tr">311076</li>
        <li class="col3 tr">38.33658</li>
        <li class="col4 tr">20</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1359034'">
        <li class="col0">16</li>
        <li class="col1">
            <p class="first-line">独行月球</p>
            <p class="second-line">2022-07-29 上映</p>
        </li>
        <li class="col2 tr">310301</li>
        <li class="col3 tr">41.60609</li>
        <li class="col4 tr">12</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1200486'">
        <li class="col0">17</li>
        <li class="col1">
            <p class="first-line">我不是药神</p>
            <p class="second-line">2018-07-05 上映</p>
        </li>
        <li class="col2 tr">310002</li>
        <li class="col3 tr">34.81434</li>
        <li class="col4 tr">26</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1230121'">
        <li class="col0">18</li>
        <li class="col1">
            <p class="first-line">中国机长</p>
            <p class="second-line">2019-09-30 上映</p>
        </li>
        <li class="col2 tr">291317</li>
        <li class="col3 tr">37.429123</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1328712'">
        <li class="col0">19</li>
        <li class="col1">
            <p class="first-line">我和我的家乡</p>
            <p class="second-line">2020-10-01 上映</p>
        </li>
        <li class="col2 tr">282985</li>
        <li class="col3 tr">38.755554</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248700'">
        <li class="col0">20</li>
        <li class="col1">
            <p class="first-line">速度与激情8</p>
            <p class="second-line">2017-04-14 上映</p>
        </li>
        <li class="col2 tr">267093</li>
        <li class="col3 tr">36.648827</li>
        <li class="col4 tr">30</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1433696'">
        <li class="col0">21</li>
        <li class="col1">
            <p class="first-line">这个杀手不太冷静</p>
            <p class="second-line">2022-02-01 上映</p>
        </li>
        <li class="col2 tr">262796</li>
        <li class="col3 tr">48.192722</li>
        <li class="col4 tr">14</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1212592'">
        <li class="col0">22</li>
        <li class="col1">
            <p class="first-line">西虹市首富</p>
            <p class="second-line">2018-07-27 上映</p>
        </li>
        <li class="col2 tr">254766</li>
        <li class="col3 tr">35.06266</li>
        <li class="col4 tr">28</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246083'">
        <li class="col0">23</li>
        <li class="col1">
            <p class="first-line">捉妖记</p>
            <p class="second-line">2015-07-16 上映</p>
        </li>
        <li class="col2 tr">243623</li>
        <li class="col3 tr">37.16107</li>
        <li class="col4 tr">41</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78405'">
        <li class="col0">24</li>
        <li class="col1">
            <p class="first-line">速度与激情7</p>
            <p class="second-line">2015-04-12 上映</p>
        </li>
        <li class="col2 tr">242313</li>
        <li class="col3 tr">38.856926</li>
        <li class="col4 tr">42</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248170'">
        <li class="col0">25</li>
        <li class="col1">
            <p class="first-line">复仇者联盟3：无限战争</p>
            <p class="second-line">2018-05-11 上映</p>
        </li>
        <li class="col2 tr">239051</li>
        <li class="col3 tr">38.24297</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/346272'">
        <li class="col0">26</li>
        <li class="col1">
            <p class="first-line">捉妖记2</p>
            <p class="second-line">2018-02-16 上映</p>
        </li>
        <li class="col2 tr">223723</li>
        <li class="col3 tr">38.314194</li>
        <li class="col4 tr">44</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1198214'">
        <li class="col0">27</li>
        <li class="col1">
            <p class="first-line">羞羞的铁拳</p>
            <p class="second-line">2017-09-30 上映</p>
        </li>
        <li class="col2 tr">221365</li>
        <li class="col3 tr">33.400208</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/344869'">
        <li class="col0">28</li>
        <li class="col1">
            <p class="first-line">疯狂的外星人</p>
            <p class="second-line">2019-02-05 上映</p>
        </li>
        <li class="col2 tr">221321</li>
        <li class="col3 tr">42.006607</li>
        <li class="col4 tr">30</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/249342'">
        <li class="col0">29</li>
        <li class="col1">
            <p class="first-line">海王</p>
            <p class="second-line">2018-12-07 上映</p>
        </li>
        <li class="col2 tr">201307</li>
        <li class="col3 tr">36.35835</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78379'">
        <li class="col0">30</li>
        <li class="col1">
            <p class="first-line">变形金刚4：绝迹重生</p>
            <p class="second-line">2014-06-27 上映</p>
        </li>
        <li class="col2 tr">197652</li>
        <li class="col3 tr">41.633636</li>
        <li class="col4 tr">50</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/344929'">
        <li class="col0">31</li>
        <li class="col1">
            <p class="first-line">前任3：再见前任</p>
            <p class="second-line">2017-12-29 上映</p>
        </li>
        <li class="col2 tr">194190</li>
        <li class="col3 tr">35.06071</li>
        <li class="col4 tr">29</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/42964'">
        <li class="col0">32</li>
        <li class="col1">
            <p class="first-line">毒液：致命守护者</p>
            <p class="second-line">2018-11-09 上映</p>
        </li>
        <li class="col2 tr">187065</li>
        <li class="col3 tr">35.510277</li>
        <li class="col4 tr">17</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248933'">
        <li class="col0">33</li>
        <li class="col1">
            <p class="first-line">功夫瑜伽</p>
            <p class="second-line">2017-01-28 上映</p>
        </li>
        <li class="col2 tr">174868</li>
        <li class="col3 tr">38.17402</li>
        <li class="col4 tr">33</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1218091'">
        <li class="col0">34</li>
        <li class="col1">
            <p class="first-line">飞驰人生</p>
            <p class="second-line">2019-02-05 上映</p>
        </li>
        <li class="col2 tr">172824</li>
        <li class="col3 tr">41.692364</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/243'">
        <li class="col0">35</li>
        <li class="col1">
            <p class="first-line">阿凡达</p>
            <p class="second-line">2010-01-04 上映</p>
        </li>
        <li class="col2 tr">171538</li>
        <li class="col3 tr">45.51871</li>
        <li class="col4 tr">22</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1397016'">
        <li class="col0">36</li>
        <li class="col1">
            <p class="first-line">人生大事</p>
            <p class="second-line">2022-06-24 上映</p>
        </li>
        <li class="col2 tr">171249</li>
        <li class="col3 tr">40.257015</li>
        <li class="col4 tr">10</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1243361'">
        <li class="col0">37</li>
        <li class="col1">
            <p class="first-line">烈火英雄</p>
            <p class="second-line">2019-08-01 上映</p>
        </li>
        <li class="col2 tr">170685</li>
        <li class="col3 tr">35.896545</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78461'">
        <li class="col0">38</li>
        <li class="col1">
            <p class="first-line">阿凡达：水之道</p>
            <p class="second-line">2022-12-16 上映</p>
        </li>
        <li class="col2 tr">169743</li>
        <li class="col3 tr">50.153454</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341628'">
        <li class="col0">39</li>
        <li class="col1">
            <p class="first-line">侏罗纪世界2</p>
            <p class="second-line">2018-06-15 上映</p>
        </li>
        <li class="col2 tr">169591</li>
        <li class="col3 tr">35.697067</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78701'">
        <li class="col0">40</li>
        <li class="col1">
            <p class="first-line">寻龙诀</p>
            <p class="second-line">2015-12-18 上映</p>
        </li>
        <li class="col2 tr">167988</li>
        <li class="col3 tr">36.200695</li>
        <li class="col4 tr">40</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248904'">
        <li class="col0">41</li>
        <li class="col1">
            <p class="first-line">西游伏妖篇</p>
            <p class="second-line">2017-01-28 上映</p>
        </li>
        <li class="col2 tr">165207</li>
        <li class="col3 tr">39.149124</li>
        <li class="col4 tr">36</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246577'">
        <li class="col0">42</li>
        <li class="col1">
            <p class="first-line">港囧</p>
            <p class="second-line">2015-09-25 上映</p>
        </li>
        <li class="col2 tr">161135</li>
        <li class="col3 tr">32.852345</li>
        <li class="col4 tr">40</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1211269'">
        <li class="col0">43</li>
        <li class="col1">
            <p class="first-line">姜子牙</p>
            <p class="second-line">2020-10-01 上映</p>
        </li>
        <li class="col2 tr">160296</li>
        <li class="col3 tr">39.791046</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1224712'">
        <li class="col0">44</li>
        <li class="col1">
            <p class="first-line">万里归途</p>
            <p class="second-line">2022-09-30 上映</p>
        </li>
        <li class="col2 tr">159316</li>
        <li class="col3 tr">41.96256</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1218029'">
        <li class="col0">45</li>
        <li class="col1">
            <p class="first-line">少年的你</p>
            <p class="second-line">2019-10-25 上映</p>
        </li>
        <li class="col2 tr">155826</li>
        <li class="col3 tr">36.217823</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248645'">
        <li class="col0">46</li>
        <li class="col1">
            <p class="first-line">变形金刚5：最后的骑士</p>
            <p class="second-line">2017-06-23 上映</p>
        </li>
        <li class="col2 tr">155126</li>
        <li class="col3 tr">36.93777</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246286'">
        <li class="col0">47</li>
        <li class="col1">
            <p class="first-line">疯狂动物城</p>
            <p class="second-line">2016-03-04 上映</p>
        </li>
        <li class="col2 tr">153190</li>
        <li class="col3 tr">33.580685</li>
        <li class="col4 tr">28</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1479130'">
        <li class="col0">48</li>
        <li class="col1">
            <p class="first-line">熊出没·伴我“熊芯”</p>
            <p class="second-line">2023-01-22 上映</p>
        </li>
        <li class="col2 tr">149518</li>
        <li class="col3 tr">46.303238</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1417305'">
        <li class="col0">49</li>
        <li class="col1">
            <p class="first-line">我和我的父辈</p>
            <p class="second-line">2021-09-30 上映</p>
        </li>
        <li class="col2 tr">147719</li>
        <li class="col3 tr">43.45881</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78421'">
        <li class="col0">50</li>
        <li class="col1">
            <p class="first-line">魔兽</p>
            <p class="second-line">2016-06-08 上映</p>
        </li>
        <li class="col2 tr">146887</li>
        <li class="col3 tr">37.072163</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78429'">
        <li class="col0">51</li>
        <li class="col1">
            <p class="first-line">复仇者联盟2：奥创纪元</p>
            <p class="second-line">2015-05-12 上映</p>
        </li>
        <li class="col2 tr">146118</li>
        <li class="col3 tr">39.999035</li>
        <li class="col4 tr">29</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246082'">
        <li class="col0">52</li>
        <li class="col1">
            <p class="first-line">夏洛特烦恼</p>
            <p class="second-line">2015-09-30 上映</p>
        </li>
        <li class="col2 tr">144475</li>
        <li class="col3 tr">32.15511</li>
        <li class="col4 tr">33</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1215605'">
        <li class="col0">53</li>
        <li class="col1">
            <p class="first-line">速度与激情：特别行动</p>
            <p class="second-line">2019-08-23 上映</p>
        </li>
        <li class="col2 tr">143495</li>
        <li class="col3 tr">35.66835</li>
        <li class="col4 tr">15</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1334342'">
        <li class="col0">54</li>
        <li class="col1">
            <p class="first-line">送你一朵小红花</p>
            <p class="second-line">2020-12-31 上映</p>
        </li>
        <li class="col2 tr">143269</li>
        <li class="col3 tr">37.269688</li>
        <li class="col4 tr">12</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1170264'">
        <li class="col0">55</li>
        <li class="col1">
            <p class="first-line">芳华</p>
            <p class="second-line">2017-12-15 上映</p>
        </li>
        <li class="col2 tr">142299</li>
        <li class="col3 tr">34.23472</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78602'">
        <li class="col0">56</li>
        <li class="col1">
            <p class="first-line">侏罗纪世界</p>
            <p class="second-line">2015-06-10 上映</p>
        </li>
        <li class="col2 tr">141821</li>
        <li class="col3 tr">38.28785</li>
        <li class="col4 tr">33</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1198925'">
        <li class="col0">57</li>
        <li class="col1">
            <p class="first-line">蜘蛛侠：英雄远征</p>
            <p class="second-line">2019-06-28 上映</p>
        </li>
        <li class="col2 tr">141767</li>
        <li class="col3 tr">35.90006</li>
        <li class="col4 tr">17</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341178'">
        <li class="col0">58</li>
        <li class="col1">
            <p class="first-line">头号玩家</p>
            <p class="second-line">2018-03-30 上映</p>
        </li>
        <li class="col2 tr">139668</li>
        <li class="col3 tr">36.40283</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/343034'">
        <li class="col0">59</li>
        <li class="col1">
            <p class="first-line">速度与激情9</p>
            <p class="second-line">2021-05-21 上映</p>
        </li>
        <li class="col2 tr">139220</li>
        <li class="col3 tr">39.293976</li>
        <li class="col4 tr">13</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1383307'">
        <li class="col0">60</li>
        <li class="col1">
            <p class="first-line">奇迹·笨小孩</p>
            <p class="second-line">2022-02-01 上映</p>
        </li>
        <li class="col2 tr">137929</li>
        <li class="col3 tr">46.259357</li>
        <li class="col4 tr">11</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/267'">
        <li class="col0">61</li>
        <li class="col1">
            <p class="first-line">泰坦尼克号</p>
            <p class="second-line">1998-04-03 上映</p>
        </li>
        <li class="col2 tr">136530</li>
        <li class="col3 tr">22.05698</li>
        <li class="col4 tr">61</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/343720'">
        <li class="col0">62</li>
        <li class="col1">
            <p class="first-line">后来的我们</p>
            <p class="second-line">2018-04-28 上映</p>
        </li>
        <li class="col2 tr">136155</li>
        <li class="col3 tr">33.90266</li>
        <li class="col4 tr">21</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1203084'">
        <li class="col0">63</li>
        <li class="col1">
            <p class="first-line">一出好戏</p>
            <p class="second-line">2018-08-10 上映</p>
        </li>
        <li class="col2 tr">135507</li>
        <li class="col3 tr">34.711494</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1218273'">
        <li class="col0">64</li>
        <li class="col1">
            <p class="first-line">误杀</p>
            <p class="second-line">2019-12-13 上映</p>
        </li>
        <li class="col2 tr">133312</li>
        <li class="col3 tr">33.156662</li>
        <li class="col4 tr">11</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1218188'">
        <li class="col0">65</li>
        <li class="col1">
            <p class="first-line">怒火·重案</p>
            <p class="second-line">2021-07-30 上映</p>
        </li>
        <li class="col2 tr">132927</li>
        <li class="col3 tr">38.70483</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1337700'">
        <li class="col0">66</li>
        <li class="col1">
            <p class="first-line">中国医生</p>
            <p class="second-line">2021-07-09 上映</p>
        </li>
        <li class="col2 tr">132877</li>
        <li class="col3 tr">36.341766</li>
        <li class="col4 tr">11</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1218142'">
        <li class="col0">67</li>
        <li class="col1">
            <p class="first-line">拆弹专家2</p>
            <p class="second-line">2020-12-24 上映</p>
        </li>
        <li class="col2 tr">131465</li>
        <li class="col3 tr">38.657715</li>
        <li class="col4 tr">11</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1218141'">
        <li class="col0">68</li>
        <li class="col1">
            <p class="first-line">扫毒2天地对决</p>
            <p class="second-line">2019-07-05 上映</p>
        </li>
        <li class="col2 tr">131288</li>
        <li class="col3 tr">36.361706</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/588362'">
        <li class="col0">69</li>
        <li class="col1">
            <p class="first-line">摔跤吧！爸爸</p>
            <p class="second-line">2017-05-05 上映</p>
        </li>
        <li class="col2 tr">129932</li>
        <li class="col3 tr">30.073994</li>
        <li class="col4 tr">22</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/342166'">
        <li class="col0">70</li>
        <li class="col1">
            <p class="first-line">无双</p>
            <p class="second-line">2018-09-30 上映</p>
        </li>
        <li class="col2 tr">127378</li>
        <li class="col3 tr">35.56216</li>
        <li class="col4 tr">15</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/938'">
        <li class="col0">71</li>
        <li class="col1">
            <p class="first-line">人再囧途之泰囧</p>
            <p class="second-line">2012-12-12 上映</p>
        </li>
        <li class="col2 tr">127096</li>
        <li class="col3 tr">32.42341</li>
        <li class="col4 tr">45</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78003'">
        <li class="col0">72</li>
        <li class="col1">
            <p class="first-line">西游·降魔篇</p>
            <p class="second-line">2013-02-10 上映</p>
        </li>
        <li class="col2 tr">124695</li>
        <li class="col3 tr">40.226612</li>
        <li class="col4 tr">41</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341737'">
        <li class="col0">73</li>
        <li class="col1">
            <p class="first-line">碟中谍6：全面瓦解</p>
            <p class="second-line">2018-08-31 上映</p>
        </li>
        <li class="col2 tr">124523</li>
        <li class="col3 tr">36.820988</li>
        <li class="col4 tr">15</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246234'">
        <li class="col0">74</li>
        <li class="col1">
            <p class="first-line">美国队长3</p>
            <p class="second-line">2016-05-06 上映</p>
        </li>
        <li class="col2 tr">124397</li>
        <li class="col3 tr">34.987694</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/343568'">
        <li class="col0">75</li>
        <li class="col1">
            <p class="first-line">哥斯拉大战金刚</p>
            <p class="second-line">2021-03-26 上映</p>
        </li>
        <li class="col2 tr">123257</li>
        <li class="col3 tr">37.444496</li>
        <li class="col4 tr">9</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/342068'">
        <li class="col0">76</li>
        <li class="col1">
            <p class="first-line">寻梦环游记</p>
            <p class="second-line">2017-11-24 上映</p>
        </li>
        <li class="col2 tr">123008</li>
        <li class="col3 tr">33.49183</li>
        <li class="col4 tr">17</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/79202'">
        <li class="col0">77</li>
        <li class="col1">
            <p class="first-line">西游记之孙悟空三打白骨精</p>
            <p class="second-line">2016-02-08 上映</p>
        </li>
        <li class="col2 tr">119854</li>
        <li class="col3 tr">36.662888</li>
        <li class="col4 tr">36</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1298367'">
        <li class="col0">78</li>
        <li class="col1">
            <p class="first-line">悬崖之上</p>
            <p class="second-line">2021-04-30 上映</p>
        </li>
        <li class="col2 tr">119149</li>
        <li class="col3 tr">38.566544</li>
        <li class="col4 tr">12</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/338391'">
        <li class="col0">79</li>
        <li class="col1">
            <p class="first-line">湄公河行动</p>
            <p class="second-line">2016-09-30 上映</p>
        </li>
        <li class="col2 tr">118685</li>
        <li class="col3 tr">30.444935</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1190122'">
        <li class="col0">80</li>
        <li class="col1">
            <p class="first-line">叶问4：完结篇</p>
            <p class="second-line">2019-12-20 上映</p>
        </li>
        <li class="col2 tr">118170</li>
        <li class="col3 tr">35.41724</li>
        <li class="col4 tr">11</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246012'">
        <li class="col0">81</li>
        <li class="col1">
            <p class="first-line">加勒比海盗5：死无对证</p>
            <p class="second-line">2017-05-26 上映</p>
        </li>
        <li class="col2 tr">118007</li>
        <li class="col3 tr">35.81335</li>
        <li class="col4 tr">22</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246267'">
        <li class="col0">82</li>
        <li class="col1">
            <p class="first-line">长城</p>
            <p class="second-line">2016-12-16 上映</p>
        </li>
        <li class="col2 tr">117311</li>
        <li class="col3 tr">35.158714</li>
        <li class="col4 tr">21</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78612'">
        <li class="col0">83</li>
        <li class="col1">
            <p class="first-line">心花路放</p>
            <p class="second-line">2014-09-30 上映</p>
        </li>
        <li class="col2 tr">116958</li>
        <li class="col3 tr">34.440758</li>
        <li class="col4 tr">36</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1451323'">
        <li class="col0">84</li>
        <li class="col1">
            <p class="first-line">人生路不熟</p>
            <p class="second-line">2023-04-28 上映</p>
        </li>
        <li class="col2 tr">116942</li>
        <li class="col3 tr">41.48333</li>
        <li class="col4 tr">9</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246330'">
        <li class="col0">85</li>
        <li class="col1">
            <p class="first-line">煎饼侠</p>
            <p class="second-line">2015-07-17 上映</p>
        </li>
        <li class="col2 tr">116018</li>
        <li class="col3 tr">32.674587</li>
        <li class="col4 tr">39</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/249898'">
        <li class="col0">86</li>
        <li class="col1">
            <p class="first-line">金刚：骷髅岛</p>
            <p class="second-line">2017-03-24 上映</p>
        </li>
        <li class="col2 tr">115892</li>
        <li class="col3 tr">35.14932</li>
        <li class="col4 tr">20</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1206875'">
        <li class="col0">87</li>
        <li class="col1">
            <p class="first-line">大黄蜂</p>
            <p class="second-line">2019-01-04 上映</p>
        </li>
        <li class="col2 tr">114973</li>
        <li class="col3 tr">35.910618</li>
        <li class="col4 tr">11</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1339160'">
        <li class="col0">88</li>
        <li class="col1">
            <p class="first-line">金刚川</p>
            <p class="second-line">2020-10-23 上映</p>
        </li>
        <li class="col2 tr">112697</li>
        <li class="col3 tr">36.991623</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/334590'">
        <li class="col0">89</li>
        <li class="col1">
            <p class="first-line">极限特工：终极回归</p>
            <p class="second-line">2017-02-10 上映</p>
        </li>
        <li class="col2 tr">112517</li>
        <li class="col3 tr">36.20821</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1331661'">
        <li class="col0">90</li>
        <li class="col1">
            <p class="first-line">误杀2</p>
            <p class="second-line">2021-12-17 上映</p>
        </li>
        <li class="col2 tr">112143</li>
        <li class="col3 tr">39.25772</li>
        <li class="col4 tr">9</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248006'">
        <li class="col0">91</li>
        <li class="col1">
            <p class="first-line">澳门风云3</p>
            <p class="second-line">2016-02-08 上映</p>
        </li>
        <li class="col2 tr">111640</li>
        <li class="col3 tr">35.636642</li>
        <li class="col4 tr">36</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246065'">
        <li class="col0">92</li>
        <li class="col1">
            <p class="first-line">生化危机：终章</p>
            <p class="second-line">2017-02-24 上映</p>
        </li>
        <li class="col2 tr">110949</li>
        <li class="col3 tr">34.683666</li>
        <li class="col4 tr">20</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1250700'">
        <li class="col0">93</li>
        <li class="col1">
            <p class="first-line">攀登者</p>
            <p class="second-line">2019-09-30 上映</p>
        </li>
        <li class="col2 tr">110433</li>
        <li class="col3 tr">36.990734</li>
        <li class="col4 tr">21</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/47'">
        <li class="col0">94</li>
        <li class="col1">
            <p class="first-line">变形金刚3</p>
            <p class="second-line">2011-07-21 上映</p>
        </li>
        <li class="col2 tr">107095</li>
        <li class="col3 tr">41.80155</li>
        <li class="col4 tr">54</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1187439'">
        <li class="col0">95</li>
        <li class="col1">
            <p class="first-line">侏罗纪世界3</p>
            <p class="second-line">2022-06-10 上映</p>
        </li>
        <li class="col2 tr">105938</li>
        <li class="col3 tr">35.55877</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/346178'">
        <li class="col0">96</li>
        <li class="col1">
            <p class="first-line">巨齿鲨</p>
            <p class="second-line">2018-08-10 上映</p>
        </li>
        <li class="col2 tr">105373</li>
        <li class="col3 tr">38.287136</li>
        <li class="col4 tr">21</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1170255'">
        <li class="col0">97</li>
        <li class="col1">
            <p class="first-line">乘风破浪</p>
            <p class="second-line">2017-01-28 上映</p>
        </li>
        <li class="col2 tr">104605</li>
        <li class="col3 tr">36.31127</li>
        <li class="col4 tr">27</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/589'">
        <li class="col0">98</li>
        <li class="col1">
            <p class="first-line">西游记之大闹天宫</p>
            <p class="second-line">2014-01-31 上映</p>
        </li>
        <li class="col2 tr">104499</li>
        <li class="col3 tr">41.9303</li>
        <li class="col4 tr">40</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/249900'">
        <li class="col0">99</li>
        <li class="col1">
            <p class="first-line">神偷奶爸3</p>
            <p class="second-line">2017-07-07 上映</p>
        </li>
        <li class="col2 tr">103791</li>
        <li class="col3 tr">34.05838</li>
        <li class="col4 tr">20</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1048268'">
        <li class="col0">100</li>
        <li class="col1">
            <p class="first-line">刺杀小说家</p>
            <p class="second-line">2021-02-12 上映</p>
        </li>
        <li class="col2 tr">103518</li>
        <li class="col3 tr">47.2659</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341139'">
        <li class="col0">101</li>
        <li class="col1">
            <p class="first-line">惊奇队长</p>
            <p class="second-line">2019-03-08 上映</p>
        </li>
        <li class="col2 tr">103517</li>
        <li class="col3 tr">37.17917</li>
        <li class="col4 tr">14</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341624'">
        <li class="col0">102</li>
        <li class="col1">
            <p class="first-line">狂暴巨兽</p>
            <p class="second-line">2018-04-13 上映</p>
        </li>
        <li class="col2 tr">100397</li>
        <li class="col3 tr">34.81579</li>
        <li class="col4 tr">13</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/79203'">
        <li class="col0">103</li>
        <li class="col1">
            <p class="first-line">盗墓笔记</p>
            <p class="second-line">2016-08-05 上映</p>
        </li>
        <li class="col2 tr">100310</li>
        <li class="col3 tr">35.231415</li>
        <li class="col4 tr">27</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78535'">
        <li class="col0">104</li>
        <li class="col1">
            <p class="first-line">功夫熊猫3</p>
            <p class="second-line">2016-01-29 上映</p>
        </li>
        <li class="col2 tr">100054</li>
        <li class="col3 tr">35.60617</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1405863'">
        <li class="col0">105</li>
        <li class="col1">
            <p class="first-line">熊出没·重返地球</p>
            <p class="second-line">2022-02-01 上映</p>
        </li>
        <li class="col2 tr">97769</li>
        <li class="col3 tr">46.636898</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246970'">
        <li class="col0">106</li>
        <li class="col1">
            <p class="first-line">奇幻森林</p>
            <p class="second-line">2016-04-15 上映</p>
        </li>
        <li class="col2 tr">97684</li>
        <li class="col3 tr">33.531403</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/79211'">
        <li class="col0">107</li>
        <li class="col1">
            <p class="first-line">澳门风云2</p>
            <p class="second-line">2015-02-19 上映</p>
        </li>
        <li class="col2 tr">97263</li>
        <li class="col3 tr">39.20782</li>
        <li class="col4 tr">36</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/343035'">
        <li class="col0">108</li>
        <li class="col1">
            <p class="first-line">速度与激情10</p>
            <p class="second-line">2023-05-17 上映</p>
        </li>
        <li class="col2 tr">97201</li>
        <li class="col3 tr">37.62267</li>
        <li class="col4 tr">9</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1216383'">
        <li class="col0">109</li>
        <li class="col1">
            <p class="first-line">比悲伤更悲伤的故事</p>
            <p class="second-line">2019-03-14 上映</p>
        </li>
        <li class="col2 tr">95843</li>
        <li class="col3 tr">30.736097</li>
        <li class="col4 tr">15</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246397'">
        <li class="col0">110</li>
        <li class="col1">
            <p class="first-line">西游记之大圣归来</p>
            <p class="second-line">2015-07-10 上映</p>
        </li>
        <li class="col2 tr">95462</li>
        <li class="col3 tr">34.659386</li>
        <li class="col4 tr">34</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246061'">
        <li class="col0">111</li>
        <li class="col1">
            <p class="first-line">哥斯拉2：怪兽之王</p>
            <p class="second-line">2019-05-31 上映</p>
        </li>
        <li class="col2 tr">93740</li>
        <li class="col3 tr">36.072906</li>
        <li class="col4 tr">14</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1444523'">
        <li class="col0">112</li>
        <li class="col1">
            <p class="first-line">穿过寒冬拥抱你</p>
            <p class="second-line">2021-12-31 上映</p>
        </li>
        <li class="col2 tr">93684</li>
        <li class="col3 tr">42.428276</li>
        <li class="col4 tr">10</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1415196'">
        <li class="col0">113</li>
        <li class="col1">
            <p class="first-line">无名</p>
            <p class="second-line">2023-01-22 上映</p>
        </li>
        <li class="col2 tr">93142</li>
        <li class="col3 tr">52.47435</li>
        <li class="col4 tr">17</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1413641'">
        <li class="col0">114</li>
        <li class="col1">
            <p class="first-line">扬名立万</p>
            <p class="second-line">2021-11-11 上映</p>
        </li>
        <li class="col2 tr">92669</li>
        <li class="col3 tr">38.033314</li>
        <li class="col4 tr">7</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/343521'">
        <li class="col0">115</li>
        <li class="col1">
            <p class="first-line">深海</p>
            <p class="second-line">2023-01-22 上映</p>
        </li>
        <li class="col2 tr">91950</li>
        <li class="col3 tr">46.54972</li>
        <li class="col4 tr">11</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1208942'">
        <li class="col0">116</li>
        <li class="col1">
            <p class="first-line">超时空同居</p>
            <p class="second-line">2018-05-18 上映</p>
        </li>
        <li class="col2 tr">90307</li>
        <li class="col3 tr">33.010834</li>
        <li class="col4 tr">12</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246211'">
        <li class="col0">117</li>
        <li class="col1">
            <p class="first-line">老炮儿</p>
            <p class="second-line">2015-12-24 上映</p>
        </li>
        <li class="col2 tr">90116</li>
        <li class="col3 tr">31.459543</li>
        <li class="col4 tr">38</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/410629'">
        <li class="col0">118</li>
        <li class="col1">
            <p class="first-line">阿丽塔：战斗天使</p>
            <p class="second-line">2019-02-22 上映</p>
        </li>
        <li class="col2 tr">89693</li>
        <li class="col3 tr">37.834686</li>
        <li class="col4 tr">14</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246307'">
        <li class="col0">119</li>
        <li class="col1">
            <p class="first-line">绝地逃亡</p>
            <p class="second-line">2016-07-21 上映</p>
        </li>
        <li class="col2 tr">88769</li>
        <li class="col3 tr">34.733532</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78631'">
        <li class="col0">120</li>
        <li class="col1">
            <p class="first-line">智取威虎山</p>
            <p class="second-line">2014-12-23 上映</p>
        </li>
        <li class="col2 tr">88348</li>
        <li class="col3 tr">41.353405</li>
        <li class="col4 tr">28</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/893'">
        <li class="col0">121</li>
        <li class="col1">
            <p class="first-line">十二生肖</p>
            <p class="second-line">2012-12-20 上映</p>
        </li>
        <li class="col2 tr">88176</li>
        <li class="col3 tr">40.26582</li>
        <li class="col4 tr">37</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1229534'">
        <li class="col0">122</li>
        <li class="col1">
            <p class="first-line">银河补习班</p>
            <p class="second-line">2019-07-18 上映</p>
        </li>
        <li class="col2 tr">87832</li>
        <li class="col3 tr">34.11227</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78341'">
        <li class="col0">123</li>
        <li class="col1">
            <p class="first-line">星际穿越</p>
            <p class="second-line">2014-11-12 上映</p>
        </li>
        <li class="col2 tr">87697</li>
        <li class="col3 tr">35.246487</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/75090'">
        <li class="col0">124</li>
        <li class="col1">
            <p class="first-line">碟中谍5：神秘国度</p>
            <p class="second-line">2015-09-08 上映</p>
        </li>
        <li class="col2 tr">86806</li>
        <li class="col3 tr">32.779945</li>
        <li class="col4 tr">26</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1300668'">
        <li class="col0">125</li>
        <li class="col1">
            <p class="first-line">温暖的抱抱</p>
            <p class="second-line">2020-12-31 上映</p>
        </li>
        <li class="col2 tr">86414</li>
        <li class="col3 tr">37.13156</li>
        <li class="col4 tr">11</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/247949'">
        <li class="col0">126</li>
        <li class="col1">
            <p class="first-line">冰雪奇缘2</p>
            <p class="second-line">2019-11-22 上映</p>
        </li>
        <li class="col2 tr">86077</li>
        <li class="col3 tr">34.397697</li>
        <li class="col4 tr">11</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1222234'">
        <li class="col0">127</li>
        <li class="col1">
            <p class="first-line">我的姐姐</p>
            <p class="second-line">2021-04-02 上映</p>
        </li>
        <li class="col2 tr">86020</li>
        <li class="col3 tr">36.802753</li>
        <li class="col4 tr">9</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1461072'">
        <li class="col0">128</li>
        <li class="col1">
            <p class="first-line">长空之王</p>
            <p class="second-line">2023-04-28 上映</p>
        </li>
        <li class="col2 tr">83908</li>
        <li class="col3 tr">41.8965</li>
        <li class="col4 tr">10</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1217123'">
        <li class="col0">129</li>
        <li class="col1">
            <p class="first-line">夺冠</p>
            <p class="second-line">2020-09-25 上映</p>
        </li>
        <li class="col2 tr">83677</li>
        <li class="col3 tr">38.80761</li>
        <li class="col4 tr">10</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1189879'">
        <li class="col0">130</li>
        <li class="col1">
            <p class="first-line">狮子王</p>
            <p class="second-line">2019-07-12 上映</p>
        </li>
        <li class="col2 tr">83387</li>
        <li class="col3 tr">35.99164</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/343208'">
        <li class="col0">131</li>
        <li class="col1">
            <p class="first-line">蚁人2：黄蜂女现身</p>
            <p class="second-line">2018-08-24 上映</p>
        </li>
        <li class="col2 tr">83157</li>
        <li class="col3 tr">36.05231</li>
        <li class="col4 tr">15</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78536'">
        <li class="col0">132</li>
        <li class="col1">
            <p class="first-line">星球大战：原力觉醒</p>
            <p class="second-line">2016-01-09 上映</p>
        </li>
        <li class="col2 tr">82426</li>
        <li class="col3 tr">37.234848</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/247300'">
        <li class="col0">133</li>
        <li class="col1">
            <p class="first-line">唐人街探案</p>
            <p class="second-line">2015-12-31 上映</p>
        </li>
        <li class="col2 tr">82334</li>
        <li class="col3 tr">31.74618</li>
        <li class="col4 tr">33</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246390'">
        <li class="col0">134</li>
        <li class="col1">
            <p class="first-line">从你的全世界路过</p>
            <p class="second-line">2016-09-29 上映</p>
        </li>
        <li class="col2 tr">81334</li>
        <li class="col3 tr">31.217215</li>
        <li class="col4 tr">22</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1410386'">
        <li class="col0">135</li>
        <li class="col1">
            <p class="first-line">铃芽之旅</p>
            <p class="second-line">2023-03-24 上映</p>
        </li>
        <li class="col2 tr">80674</li>
        <li class="col3 tr">33.224785</li>
        <li class="col4 tr">9</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246177'">
        <li class="col0">136</li>
        <li class="col1">
            <p class="first-line">X战警：天启</p>
            <p class="second-line">2016-06-03 上映</p>
        </li>
        <li class="col2 tr">80091</li>
        <li class="col3 tr">34.448685</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1211727'">
        <li class="col0">137</li>
        <li class="col1">
            <p class="first-line">反贪风暴4</p>
            <p class="second-line">2019-04-04 上映</p>
        </li>
        <li class="col2 tr">79905</li>
        <li class="col3 tr">34.990177</li>
        <li class="col4 tr">11</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1208282'">
        <li class="col0">138</li>
        <li class="col1">
            <p class="first-line">无名之辈</p>
            <p class="second-line">2018-11-16 上映</p>
        </li>
        <li class="col2 tr">79452</li>
        <li class="col3 tr">34.597515</li>
        <li class="col4 tr">12</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1320283'">
        <li class="col0">139</li>
        <li class="col1">
            <p class="first-line">你的婚礼</p>
            <p class="second-line">2021-04-30 上映</p>
        </li>
        <li class="col2 tr">78920</li>
        <li class="col3 tr">37.587566</li>
        <li class="col4 tr">15</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/247575'">
        <li class="col0">140</li>
        <li class="col1">
            <p class="first-line">北京遇上西雅图之不二情书</p>
            <p class="second-line">2016-04-29 上映</p>
        </li>
        <li class="col2 tr">78538</li>
        <li class="col3 tr">33.515335</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/334620'">
        <li class="col0">141</li>
        <li class="col1">
            <p class="first-line">蜘蛛侠：英雄归来</p>
            <p class="second-line">2017-09-08 上映</p>
        </li>
        <li class="col2 tr">77477</li>
        <li class="col3 tr">35.15436</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/76365'">
        <li class="col0">142</li>
        <li class="col1">
            <p class="first-line">叶问3</p>
            <p class="second-line">2016-03-04 上映</p>
        </li>
        <li class="col2 tr">76948</li>
        <li class="col3 tr">38.843933</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1300936'">
        <li class="col0">143</li>
        <li class="col1">
            <p class="first-line">人潮汹涌</p>
            <p class="second-line">2021-02-12 上映</p>
        </li>
        <li class="col2 tr">76235</li>
        <li class="col3 tr">41.317875</li>
        <li class="col4 tr">10</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78464'">
        <li class="col0">144</li>
        <li class="col1">
            <p class="first-line">霍比特人3：五军之战</p>
            <p class="second-line">2015-01-23 上映</p>
        </li>
        <li class="col2 tr">76129</li>
        <li class="col3 tr">45.45982</li>
        <li class="col4 tr">30</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248935'">
        <li class="col0">145</li>
        <li class="col1">
            <p class="first-line">大闹天竺</p>
            <p class="second-line">2017-01-28 上映</p>
        </li>
        <li class="col2 tr">75611</li>
        <li class="col3 tr">35.56586</li>
        <li class="col4 tr">31</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78043'">
        <li class="col0">146</li>
        <li class="col1">
            <p class="first-line">钢铁侠3</p>
            <p class="second-line">2013-05-01 上映</p>
        </li>
        <li class="col2 tr">75486</li>
        <li class="col3 tr">41.834854</li>
        <li class="col4 tr">33</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/71946'">
        <li class="col0">147</li>
        <li class="col1">
            <p class="first-line">无问西东</p>
            <p class="second-line">2018-01-12 上映</p>
        </li>
        <li class="col2 tr">75432</li>
        <li class="col3 tr">31.431118</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246124'">
        <li class="col0">148</li>
        <li class="col1">
            <p class="first-line">奇异博士</p>
            <p class="second-line">2016-11-04 上映</p>
        </li>
        <li class="col2 tr">75020</li>
        <li class="col3 tr">34.8847</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1208122'">
        <li class="col0">149</li>
        <li class="col1">
            <p class="first-line">神秘巨星</p>
            <p class="second-line">2018-01-19 上映</p>
        </li>
        <li class="col2 tr">74708</li>
        <li class="col3 tr">30.02213</li>
        <li class="col4 tr">17</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/249894'">
        <li class="col0">150</li>
        <li class="col1">
            <p class="first-line">雷神3：诸神黄昏</p>
            <p class="second-line">2017-11-03 上映</p>
        </li>
        <li class="col2 tr">74371</li>
        <li class="col3 tr">35.466118</li>
        <li class="col4 tr">15</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/79082'">
        <li class="col0">151</li>
        <li class="col1">
            <p class="first-line">天将雄师</p>
            <p class="second-line">2015-02-19 上映</p>
        </li>
        <li class="col2 tr">74201</li>
        <li class="col3 tr">40.640205</li>
        <li class="col4 tr">38</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246377'">
        <li class="col0">152</li>
        <li class="col1">
            <p class="first-line">猩球崛起3：终极之战</p>
            <p class="second-line">2017-09-15 上映</p>
        </li>
        <li class="col2 tr">74051</li>
        <li class="col3 tr">34.9678</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/247875'">
        <li class="col0">153</li>
        <li class="col1">
            <p class="first-line">金刚狼3：殊死一战</p>
            <p class="second-line">2017-03-03 上映</p>
        </li>
        <li class="col2 tr">73008</li>
        <li class="col3 tr">32.372185</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/338463'">
        <li class="col0">154</li>
        <li class="col1">
            <p class="first-line">西游记女儿国</p>
            <p class="second-line">2018-02-16 上映</p>
        </li>
        <li class="col2 tr">72741</li>
        <li class="col3 tr">39.74682</li>
        <li class="col4 tr">33</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78356'">
        <li class="col0">155</li>
        <li class="col1">
            <p class="first-line">X战警：逆转未来</p>
            <p class="second-line">2014-05-23 上映</p>
        </li>
        <li class="col2 tr">72293</li>
        <li class="col3 tr">37.240368</li>
        <li class="col4 tr">29</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78607'">
        <li class="col0">156</li>
        <li class="col1">
            <p class="first-line">终结者：创世纪</p>
            <p class="second-line">2015-08-23 上映</p>
        </li>
        <li class="col2 tr">72240</li>
        <li class="col3 tr">36.772095</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78059'">
        <li class="col0">157</li>
        <li class="col1">
            <p class="first-line">致我们终将逝去的青春</p>
            <p class="second-line">2013-04-26 上映</p>
        </li>
        <li class="col2 tr">71902</li>
        <li class="col3 tr">31.97473</li>
        <li class="col4 tr">36</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78478'">
        <li class="col0">158</li>
        <li class="col1">
            <p class="first-line">美国队长2</p>
            <p class="second-line">2014-04-04 上映</p>
        </li>
        <li class="col2 tr">71898</li>
        <li class="col3 tr">39.05371</li>
        <li class="col4 tr">29</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1243239'">
        <li class="col0">159</li>
        <li class="col1">
            <p class="first-line">熊出没·原始时代</p>
            <p class="second-line">2019-02-05 上映</p>
        </li>
        <li class="col2 tr">71740</li>
        <li class="col3 tr">39.035553</li>
        <li class="col4 tr">22</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78226'">
        <li class="col0">160</li>
        <li class="col1">
            <p class="first-line">私人订制</p>
            <p class="second-line">2013-12-19 上映</p>
        </li>
        <li class="col2 tr">71347</li>
        <li class="col3 tr">35.469856</li>
        <li class="col4 tr">30</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1203439'">
        <li class="col0">161</li>
        <li class="col1">
            <p class="first-line">神探大战</p>
            <p class="second-line">2022-07-08 上映</p>
        </li>
        <li class="col2 tr">71211</li>
        <li class="col3 tr">37.894077</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78625'">
        <li class="col0">162</li>
        <li class="col1">
            <p class="first-line">猩球崛起2：黎明之战</p>
            <p class="second-line">2014-08-29 上映</p>
        </li>
        <li class="col2 tr">70732</li>
        <li class="col3 tr">36.77872</li>
        <li class="col4 tr">28</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1197417'">
        <li class="col0">163</li>
        <li class="col1">
            <p class="first-line">使徒行者2：谍影行动</p>
            <p class="second-line">2019-08-07 上映</p>
        </li>
        <li class="col2 tr">70228</li>
        <li class="col3 tr">36.29202</li>
        <li class="col4 tr">17</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/502'">
        <li class="col0">164</li>
        <li class="col1">
            <p class="first-line">画皮2</p>
            <p class="second-line">2012-06-28 上映</p>
        </li>
        <li class="col2 tr">70202</li>
        <li class="col3 tr">41.05247</li>
        <li class="col4 tr">37</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1434052'">
        <li class="col0">165</li>
        <li class="col1">
            <p class="first-line">保你平安</p>
            <p class="second-line">2023-03-10 上映</p>
        </li>
        <li class="col2 tr">70076</li>
        <li class="col3 tr">42.16512</li>
        <li class="col4 tr">6</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78403'">
        <li class="col0">166</li>
        <li class="col1">
            <p class="first-line">狼图腾</p>
            <p class="second-line">2015-02-19 上映</p>
        </li>
        <li class="col2 tr">70075</li>
        <li class="col3 tr">39.397194</li>
        <li class="col4 tr">34</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248916'">
        <li class="col0">167</li>
        <li class="col1">
            <p class="first-line">铁道飞虎</p>
            <p class="second-line">2016-12-23 上映</p>
        </li>
        <li class="col2 tr">69929</li>
        <li class="col3 tr">36.7024</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341375'">
        <li class="col0">168</li>
        <li class="col1">
            <p class="first-line">悟空传</p>
            <p class="second-line">2017-07-13 上映</p>
        </li>
        <li class="col2 tr">69685</li>
        <li class="col3 tr">35.916782</li>
        <li class="col4 tr">17</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78621'">
        <li class="col0">169</li>
        <li class="col1">
            <p class="first-line">爸爸去哪儿</p>
            <p class="second-line">2014-01-31 上映</p>
        </li>
        <li class="col2 tr">69652</li>
        <li class="col3 tr">31.801163</li>
        <li class="col4 tr">40</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78151'">
        <li class="col0">170</li>
        <li class="col1">
            <p class="first-line">环太平洋</p>
            <p class="second-line">2013-07-31 上映</p>
        </li>
        <li class="col2 tr">69540</li>
        <li class="col3 tr">40.411037</li>
        <li class="col4 tr">38</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341195'">
        <li class="col0">171</li>
        <li class="col1">
            <p class="first-line">正义联盟</p>
            <p class="second-line">2017-11-17 上映</p>
        </li>
        <li class="col2 tr">69058</li>
        <li class="col3 tr">35.48468</li>
        <li class="col4 tr">13</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248683'">
        <li class="col0">172</li>
        <li class="col1">
            <p class="first-line">银河护卫队2</p>
            <p class="second-line">2017-05-05 上映</p>
        </li>
        <li class="col2 tr">68615</li>
        <li class="col3 tr">37.273075</li>
        <li class="col4 tr">17</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1279731'">
        <li class="col0">173</li>
        <li class="col1">
            <p class="first-line">宠爱</p>
            <p class="second-line">2019-12-31 上映</p>
        </li>
        <li class="col2 tr">68364</li>
        <li class="col3 tr">34.891582</li>
        <li class="col4 tr">9</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246088'">
        <li class="col0">174</li>
        <li class="col1">
            <p class="first-line">九层妖塔</p>
            <p class="second-line">2015-09-30 上映</p>
        </li>
        <li class="col2 tr">68132</li>
        <li class="col3 tr">34.347466</li>
        <li class="col4 tr">30</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/249033'">
        <li class="col0">175</li>
        <li class="col1">
            <p class="first-line">明日战记</p>
            <p class="second-line">2022-08-05 上映</p>
        </li>
        <li class="col2 tr">67942</li>
        <li class="col3 tr">41.25811</li>
        <li class="col4 tr">7</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341289'">
        <li class="col0">176</li>
        <li class="col1">
            <p class="first-line">寒战2</p>
            <p class="second-line">2016-07-08 上映</p>
        </li>
        <li class="col2 tr">67661</li>
        <li class="col3 tr">36.547977</li>
        <li class="col4 tr">27</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/61'">
        <li class="col0">177</li>
        <li class="col1">
            <p class="first-line">碟中谍4</p>
            <p class="second-line">2012-01-28 上映</p>
        </li>
        <li class="col2 tr">67211</li>
        <li class="col3 tr">35.086987</li>
        <li class="col4 tr">43</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78392'">
        <li class="col0">178</li>
        <li class="col1">
            <p class="first-line">蚁人</p>
            <p class="second-line">2015-10-16 上映</p>
        </li>
        <li class="col2 tr">67035</li>
        <li class="col3 tr">36.10703</li>
        <li class="col4 tr">22</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1203528'">
        <li class="col0">179</li>
        <li class="col1">
            <p class="first-line">摩天营救</p>
            <p class="second-line">2018-07-20 上映</p>
        </li>
        <li class="col2 tr">66981</li>
        <li class="col3 tr">35.184887</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78554'">
        <li class="col0">180</li>
        <li class="col1">
            <p class="first-line">分手大师</p>
            <p class="second-line">2014-06-27 上映</p>
        </li>
        <li class="col2 tr">66509</li>
        <li class="col3 tr">33.37043</li>
        <li class="col4 tr">34</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341138'">
        <li class="col0">181</li>
        <li class="col1">
            <p class="first-line">黑豹</p>
            <p class="second-line">2018-03-09 上映</p>
        </li>
        <li class="col2 tr">66260</li>
        <li class="col3 tr">36.069355</li>
        <li class="col4 tr">17</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1188324'">
        <li class="col0">182</li>
        <li class="col1">
            <p class="first-line">情圣</p>
            <p class="second-line">2016-12-30 上映</p>
        </li>
        <li class="col2 tr">65790</li>
        <li class="col3 tr">31.282188</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1383605'">
        <li class="col0">183</li>
        <li class="col1">
            <p class="first-line">灌篮高手</p>
            <p class="second-line">2023-04-20 上映</p>
        </li>
        <li class="col2 tr">65159</li>
        <li class="col3 tr">36.246265</li>
        <li class="col4 tr">9</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/180'">
        <li class="col0">184</li>
        <li class="col1">
            <p class="first-line">唐山大地震</p>
            <p class="second-line">2010-07-22 上映</p>
        </li>
        <li class="col2 tr">65000</li>
        <li class="col3 tr">37.08052</li>
        <li class="col4 tr">63</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246581'">
        <li class="col0">185</li>
        <li class="col1">
            <p class="first-line">恶棍天使</p>
            <p class="second-line">2015-12-24 上映</p>
        </li>
        <li class="col2 tr">64854</li>
        <li class="col3 tr">29.965164</li>
        <li class="col4 tr">40</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1240159'">
        <li class="col0">186</li>
        <li class="col1">
            <p class="first-line">来电狂响</p>
            <p class="second-line">2018-12-28 上映</p>
        </li>
        <li class="col2 tr">64139</li>
        <li class="col3 tr">34.942345</li>
        <li class="col4 tr">14</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/346629'">
        <li class="col0">187</li>
        <li class="col1">
            <p class="first-line">大侦探皮卡丘</p>
            <p class="second-line">2019-05-10 上映</p>
        </li>
        <li class="col2 tr">64070</li>
        <li class="col3 tr">35.44802</li>
        <li class="col4 tr">10</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246333'">
        <li class="col0">188</li>
        <li class="col1">
            <p class="first-line">惊天魔盗团2</p>
            <p class="second-line">2016-06-24 上映</p>
        </li>
        <li class="col2 tr">63771</li>
        <li class="col3 tr">33.112507</li>
        <li class="col4 tr">27</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/182'">
        <li class="col0">189</li>
        <li class="col1">
            <p class="first-line">让子弹飞</p>
            <p class="second-line">2010-12-16 上映</p>
        </li>
        <li class="col2 tr">63675</li>
        <li class="col3 tr">39.43557</li>
        <li class="col4 tr">49</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78460'">
        <li class="col0">190</li>
        <li class="col1">
            <p class="first-line">环太平洋：雷霆再起</p>
            <p class="second-line">2018-03-23 上映</p>
        </li>
        <li class="col2 tr">63323</li>
        <li class="col3 tr">35.434902</li>
        <li class="col4 tr">13</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1203437'">
        <li class="col0">191</li>
        <li class="col1">
            <p class="first-line">影</p>
            <p class="second-line">2018-09-30 上映</p>
        </li>
        <li class="col2 tr">62899</li>
        <li class="col3 tr">35.800556</li>
        <li class="col4 tr">14</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1277950'">
        <li class="col0">192</li>
        <li class="col1">
            <p class="first-line">反贪风暴5：最终章</p>
            <p class="second-line">2021-12-31 上映</p>
        </li>
        <li class="col2 tr">62893</li>
        <li class="col3 tr">40.75184</li>
        <li class="col4 tr">9</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78697'">
        <li class="col0">193</li>
        <li class="col1">
            <p class="first-line">后会无期</p>
            <p class="second-line">2014-07-24 上映</p>
        </li>
        <li class="col2 tr">62875</li>
        <li class="col3 tr">31.956974</li>
        <li class="col4 tr">34</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246363'">
        <li class="col0">194</li>
        <li class="col1">
            <p class="first-line">末日崩塌</p>
            <p class="second-line">2015-06-02 上映</p>
        </li>
        <li class="col2 tr">62858</li>
        <li class="col3 tr">37.411068</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/580298'">
        <li class="col0">195</li>
        <li class="col1">
            <p class="first-line">新喜剧之王</p>
            <p class="second-line">2019-02-05 上映</p>
        </li>
        <li class="col2 tr">62752</li>
        <li class="col3 tr">42.586273</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/249895'">
        <li class="col0">196</li>
        <li class="col1">
            <p class="first-line">新木乃伊</p>
            <p class="second-line">2017-06-09 上映</p>
        </li>
        <li class="col2 tr">62563</li>
        <li class="col3 tr">35.19523</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78439'">
        <li class="col0">197</li>
        <li class="col1">
            <p class="first-line">蝙蝠侠大战超人：正义黎明</p>
            <p class="second-line">2016-03-25 上映</p>
        </li>
        <li class="col2 tr">61826</li>
        <li class="col3 tr">35.59753</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1202638'">
        <li class="col0">198</li>
        <li class="col1">
            <p class="first-line">失控玩家</p>
            <p class="second-line">2021-08-27 上映</p>
        </li>
        <li class="col2 tr">61257</li>
        <li class="col3 tr">38.86088</li>
        <li class="col4 tr">7</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/171'">
        <li class="col0">199</li>
        <li class="col1">
            <p class="first-line">功夫熊猫2</p>
            <p class="second-line">2011-05-28 上映</p>
        </li>
        <li class="col2 tr">61175</li>
        <li class="col3 tr">37.799377</li>
        <li class="col4 tr">42</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/247731'">
        <li class="col0">200</li>
        <li class="col1">
            <p class="first-line">神奇女侠</p>
            <p class="second-line">2017-06-02 上映</p>
        </li>
        <li class="col2 tr">61014</li>
        <li class="col3 tr">36.301155</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1367251'">
        <li class="col0">201</li>
        <li class="col1">
            <p class="first-line">狙击手</p>
            <p class="second-line">2022-02-01 上映</p>
        </li>
        <li class="col2 tr">60805</li>
        <li class="col3 tr">44.774277</li>
        <li class="col4 tr">7</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/342858'">
        <li class="col0">202</li>
        <li class="col1">
            <p class="first-line">一条狗的使命</p>
            <p class="second-line">2017-03-03 上映</p>
        </li>
        <li class="col2 tr">60777</li>
        <li class="col3 tr">29.967405</li>
        <li class="col4 tr">15</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341516'">
        <li class="col0">203</li>
        <li class="col1">
            <p class="first-line">狄仁杰之四大天王</p>
            <p class="second-line">2018-07-27 上映</p>
        </li>
        <li class="col2 tr">60636</li>
        <li class="col3 tr">39.113647</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1211482'">
        <li class="col0">204</li>
        <li class="col1">
            <p class="first-line">熊出没·变形记</p>
            <p class="second-line">2018-02-16 上映</p>
        </li>
        <li class="col2 tr">60552</li>
        <li class="col3 tr">35.826714</li>
        <li class="col4 tr">29</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/334722'">
        <li class="col0">205</li>
        <li class="col1">
            <p class="first-line">使徒行者</p>
            <p class="second-line">2016-08-11 上映</p>
        </li>
        <li class="col2 tr">60538</li>
        <li class="col3 tr">29.397415</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1217402'">
        <li class="col0">206</li>
        <li class="col1">
            <p class="first-line">李茶的姑妈</p>
            <p class="second-line">2018-09-30 上映</p>
        </li>
        <li class="col2 tr">60438</li>
        <li class="col3 tr">34.69147</li>
        <li class="col4 tr">15</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341224'">
        <li class="col0">207</li>
        <li class="col1">
            <p class="first-line">银河护卫队3</p>
            <p class="second-line">2023-05-05 上映</p>
        </li>
        <li class="col2 tr">60428</li>
        <li class="col3 tr">39.278805</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78198'">
        <li class="col0">208</li>
        <li class="col1">
            <p class="first-line">狄仁杰之神都龙王</p>
            <p class="second-line">2013-09-28 上映</p>
        </li>
        <li class="col2 tr">60059</li>
        <li class="col3 tr">40.039875</li>
        <li class="col4 tr">30</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78336'">
        <li class="col0">209</li>
        <li class="col1">
            <p class="first-line">银河护卫队</p>
            <p class="second-line">2014-10-10 上映</p>
        </li>
        <li class="col2 tr">59640</li>
        <li class="col3 tr">38.591774</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1298938'">
        <li class="col0">210</li>
        <li class="col1">
            <p class="first-line">熊出没·狂野大陆</p>
            <p class="second-line">2021-02-12 上映</p>
        </li>
        <li class="col2 tr">59529</li>
        <li class="col3 tr">43.313347</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/28'">
        <li class="col0">211</li>
        <li class="col1">
            <p class="first-line">金陵十三钗</p>
            <p class="second-line">2011-12-15 上映</p>
        </li>
        <li class="col2 tr">59214</li>
        <li class="col3 tr">41.266125</li>
        <li class="col4 tr">40</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248918'">
        <li class="col0">212</li>
        <li class="col1">
            <p class="first-line">神奇动物在哪里</p>
            <p class="second-line">2016-11-25 上映</p>
        </li>
        <li class="col2 tr">59085</li>
        <li class="col3 tr">34.902664</li>
        <li class="col4 tr">21</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/247658'">
        <li class="col0">213</li>
        <li class="col1">
            <p class="first-line">美女与野兽</p>
            <p class="second-line">2017-03-17 上映</p>
        </li>
        <li class="col2 tr">59040</li>
        <li class="col3 tr">35.080605</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/245980'">
        <li class="col0">214</li>
        <li class="col1">
            <p class="first-line">匆匆那年</p>
            <p class="second-line">2014-12-05 上映</p>
        </li>
        <li class="col2 tr">58861</li>
        <li class="col3 tr">34.74073</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246369'">
        <li class="col0">215</li>
        <li class="col1">
            <p class="first-line">火星救援</p>
            <p class="second-line">2015-11-25 上映</p>
        </li>
        <li class="col2 tr">58571</li>
        <li class="col3 tr">36.772423</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78515'">
        <li class="col0">216</li>
        <li class="col1">
            <p class="first-line">超凡蜘蛛侠2</p>
            <p class="second-line">2014-05-04 上映</p>
        </li>
        <li class="col2 tr">58538</li>
        <li class="col3 tr">38.662636</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/771'">
        <li class="col0">217</li>
        <li class="col1">
            <p class="first-line">2012</p>
            <p class="second-line">2009-11-13 上映</p>
        </li>
        <li class="col2 tr">58444</li>
        <li class="col3 tr">33.303165</li>
        <li class="col4 tr">46</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/248566'">
        <li class="col0">218</li>
        <li class="col1">
            <p class="first-line">邪不压正</p>
            <p class="second-line">2018-07-13 上映</p>
        </li>
        <li class="col2 tr">58352</li>
        <li class="col3 tr">35.564896</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1298542'">
        <li class="col0">219</li>
        <li class="col1">
            <p class="first-line">白蛇2：青蛇劫起</p>
            <p class="second-line">2021-07-23 上映</p>
        </li>
        <li class="col2 tr">58021</li>
        <li class="col3 tr">39.02653</li>
        <li class="col4 tr">7</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1176763'">
        <li class="col0">220</li>
        <li class="col1">
            <p class="first-line">追龙</p>
            <p class="second-line">2017-09-30 上映</p>
        </li>
        <li class="col2 tr">57726</li>
        <li class="col3 tr">32.49085</li>
        <li class="col4 tr">20</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/344881'">
        <li class="col0">221</li>
        <li class="col1">
            <p class="first-line">你的名字。</p>
            <p class="second-line">2016-12-02 上映</p>
        </li>
        <li class="col2 tr">57571</li>
        <li class="col3 tr">27.830141</li>
        <li class="col4 tr">22</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246591'">
        <li class="col0">222</li>
        <li class="col1">
            <p class="first-line">大鱼海棠</p>
            <p class="second-line">2016-07-08 上映</p>
        </li>
        <li class="col2 tr">57378</li>
        <li class="col3 tr">32.934837</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/995'">
        <li class="col0">223</li>
        <li class="col1">
            <p class="first-line">少年派的奇幻漂流</p>
            <p class="second-line">2012-11-22 上映</p>
        </li>
        <li class="col2 tr">57288</li>
        <li class="col3 tr">39.428986</li>
        <li class="col4 tr">38</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/262'">
        <li class="col0">224</li>
        <li class="col1">
            <p class="first-line">复仇者联盟</p>
            <p class="second-line">2012-05-05 上映</p>
        </li>
        <li class="col2 tr">56827</li>
        <li class="col3 tr">41.705013</li>
        <li class="col4 tr">33</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246909'">
        <li class="col0">225</li>
        <li class="col1">
            <p class="first-line">杀破狼2</p>
            <p class="second-line">2015-06-18 上映</p>
        </li>
        <li class="col2 tr">55966</li>
        <li class="col3 tr">36.174625</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1407233'">
        <li class="col0">226</li>
        <li class="col1">
            <p class="first-line">新神榜：杨戬</p>
            <p class="second-line">2022-08-19 上映</p>
        </li>
        <li class="col2 tr">55550</li>
        <li class="col3 tr">42.119488</li>
        <li class="col4 tr">5</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1175253'">
        <li class="col0">227</li>
        <li class="col1">
            <p class="first-line">爱情公寓</p>
            <p class="second-line">2018-08-10 上映</p>
        </li>
        <li class="col2 tr">55545</li>
        <li class="col3 tr">35.352978</li>
        <li class="col4 tr">27</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1335230'">
        <li class="col0">228</li>
        <li class="col1">
            <p class="first-line">哥，你好</p>
            <p class="second-line">2022-09-09 上映</p>
        </li>
        <li class="col2 tr">54798</li>
        <li class="col3 tr">41.639717</li>
        <li class="col4 tr">4</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78304'">
        <li class="col0">229</li>
        <li class="col1">
            <p class="first-line">战狼</p>
            <p class="second-line">2015-04-02 上映</p>
        </li>
        <li class="col2 tr">54469</li>
        <li class="col3 tr">34.260075</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1389048'">
        <li class="col0">230</li>
        <li class="col1">
            <p class="first-line">四海</p>
            <p class="second-line">2022-02-01 上映</p>
        </li>
        <li class="col2 tr">54277</li>
        <li class="col3 tr">53.10559</li>
        <li class="col4 tr">17</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78617'">
        <li class="col0">231</li>
        <li class="col1">
            <p class="first-line">007：幽灵党</p>
            <p class="second-line">2015-11-13 上映</p>
        </li>
        <li class="col2 tr">54113</li>
        <li class="col3 tr">31.537039</li>
        <li class="col4 tr">28</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78068'">
        <li class="col0">232</li>
        <li class="col1">
            <p class="first-line">中国合伙人</p>
            <p class="second-line">2013-05-17 上映</p>
        </li>
        <li class="col2 tr">54064</li>
        <li class="col3 tr">32.145626</li>
        <li class="col4 tr">27</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/27'">
        <li class="col0">233</li>
        <li class="col1">
            <p class="first-line">龙门飞甲</p>
            <p class="second-line">2011-12-15 上映</p>
        </li>
        <li class="col2 tr">53992</li>
        <li class="col3 tr">44.14197</li>
        <li class="col4 tr">35</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/345420'">
        <li class="col0">234</li>
        <li class="col1">
            <p class="first-line">英伦对决</p>
            <p class="second-line">2017-09-30 上映</p>
        </li>
        <li class="col2 tr">53983</li>
        <li class="col3 tr">37.63522</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1240838'">
        <li class="col0">235</li>
        <li class="col1">
            <p class="first-line">除暴</p>
            <p class="second-line">2020-11-20 上映</p>
        </li>
        <li class="col2 tr">53821</li>
        <li class="col3 tr">37.087032</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246896'">
        <li class="col0">236</li>
        <li class="col1">
            <p class="first-line">三生三世十里桃花</p>
            <p class="second-line">2017-08-03 上映</p>
        </li>
        <li class="col2 tr">53501</li>
        <li class="col3 tr">35.14003</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/77192'">
        <li class="col0">237</li>
        <li class="col1">
            <p class="first-line">警察故事2013</p>
            <p class="second-line">2013-12-24 上映</p>
        </li>
        <li class="col2 tr">53406</li>
        <li class="col3 tr">39.545963</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/345862'">
        <li class="col0">238</li>
        <li class="col1">
            <p class="first-line">妖猫传</p>
            <p class="second-line">2017-12-22 上映</p>
        </li>
        <li class="col2 tr">53026</li>
        <li class="col3 tr">35.54714</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78525'">
        <li class="col0">239</li>
        <li class="col1">
            <p class="first-line">哆啦A梦：伴我同行</p>
            <p class="second-line">2015-05-28 上映</p>
        </li>
        <li class="col2 tr">52916</li>
        <li class="col3 tr">34.66687</li>
        <li class="col4 tr">22</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/79232'">
        <li class="col0">240</li>
        <li class="col1">
            <p class="first-line">超能陆战队</p>
            <p class="second-line">2015-02-28 上映</p>
        </li>
        <li class="col2 tr">52625</li>
        <li class="col3 tr">36.70751</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78283'">
        <li class="col0">241</li>
        <li class="col1">
            <p class="first-line">澳门风云</p>
            <p class="second-line">2014-01-31 上映</p>
        </li>
        <li class="col2 tr">52471</li>
        <li class="col3 tr">32.365917</li>
        <li class="col4 tr">31</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/342176'">
        <li class="col0">242</li>
        <li class="col1">
            <p class="first-line">杀破狼·贪狼</p>
            <p class="second-line">2017-08-17 上映</p>
        </li>
        <li class="col2 tr">52291</li>
        <li class="col3 tr">32.32158</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1189089'">
        <li class="col0">243</li>
        <li class="col1">
            <p class="first-line">熊出没·奇幻空间</p>
            <p class="second-line">2017-01-28 上映</p>
        </li>
        <li class="col2 tr">52114</li>
        <li class="col3 tr">34.320858</li>
        <li class="col4 tr">27</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78487'">
        <li class="col0">244</li>
        <li class="col1">
            <p class="first-line">小时代3：刺金时代</p>
            <p class="second-line">2014-07-17 上映</p>
        </li>
        <li class="col2 tr">52098</li>
        <li class="col3 tr">31.580196</li>
        <li class="col4 tr">33</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78041'">
        <li class="col0">245</li>
        <li class="col1">
            <p class="first-line">北京遇上西雅图</p>
            <p class="second-line">2013-03-21 上映</p>
        </li>
        <li class="col2 tr">52013</li>
        <li class="col3 tr">31.550077</li>
        <li class="col4 tr">31</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78222'">
        <li class="col0">246</li>
        <li class="col1">
            <p class="first-line">一步之遥</p>
            <p class="second-line">2014-12-18 上映</p>
        </li>
        <li class="col2 tr">51376</li>
        <li class="col3 tr">42.4509</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246188'">
        <li class="col0">247</li>
        <li class="col1">
            <p class="first-line">愤怒的小鸟</p>
            <p class="second-line">2016-05-20 上映</p>
        </li>
        <li class="col2 tr">51297</li>
        <li class="col3 tr">31.765776</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246505'">
        <li class="col0">248</li>
        <li class="col1">
            <p class="first-line">滚蛋吧！肿瘤君</p>
            <p class="second-line">2015-08-13 上映</p>
        </li>
        <li class="col2 tr">51045</li>
        <li class="col3 tr">33.640533</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1198178'">
        <li class="col0">249</li>
        <li class="col1">
            <p class="first-line">动物世界</p>
            <p class="second-line">2018-06-29 上映</p>
        </li>
        <li class="col2 tr">50967</li>
        <li class="col3 tr">36.847546</li>
        <li class="col4 tr">13</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/489894'">
        <li class="col0">250</li>
        <li class="col1">
            <p class="first-line">我在时间尽头等你</p>
            <p class="second-line">2020-08-25 上映</p>
        </li>
        <li class="col2 tr">50541</li>
        <li class="col3 tr">35.25256</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1336183'">
        <li class="col0">251</li>
        <li class="col1">
            <p class="first-line">1921</p>
            <p class="second-line">2021-07-01 上映</p>
        </li>
        <li class="col2 tr">50474</li>
        <li class="col3 tr">34.85736</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/389'">
        <li class="col0">252</li>
        <li class="col1">
            <p class="first-line">黑衣人3</p>
            <p class="second-line">2012-05-25 上映</p>
        </li>
        <li class="col2 tr">50345</li>
        <li class="col3 tr">40.718327</li>
        <li class="col4 tr">28</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246375'">
        <li class="col0">253</li>
        <li class="col1">
            <p class="first-line">独立日：卷土重来</p>
            <p class="second-line">2016-06-24 上映</p>
        </li>
        <li class="col2 tr">50219</li>
        <li class="col3 tr">35.726177</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/257739'">
        <li class="col0">254</li>
        <li class="col1">
            <p class="first-line">古墓丽影：源起之战</p>
            <p class="second-line">2018-03-16 上映</p>
        </li>
        <li class="col2 tr">49748</li>
        <li class="col3 tr">35.066303</li>
        <li class="col4 tr">14</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/416'">
        <li class="col0">255</li>
        <li class="col1">
            <p class="first-line">盗梦空间</p>
            <p class="second-line">2010-09-01 上映</p>
        </li>
        <li class="col2 tr">49620</li>
        <li class="col3 tr">30.196941</li>
        <li class="col4 tr">40</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341897'">
        <li class="col0">256</li>
        <li class="col1">
            <p class="first-line">勇敢者游戏：决战丛林</p>
            <p class="second-line">2018-01-12 上映</p>
        </li>
        <li class="col2 tr">49196</li>
        <li class="col3 tr">34.19796</li>
        <li class="col4 tr">18</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1212'">
        <li class="col0">257</li>
        <li class="col1">
            <p class="first-line">千与千寻</p>
            <p class="second-line">2019-06-21 上映</p>
        </li>
        <li class="col2 tr">48828</li>
        <li class="col3 tr">31.226898</li>
        <li class="col4 tr">12</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/461076'">
        <li class="col0">258</li>
        <li class="col1">
            <p class="first-line">紧急救援</p>
            <p class="second-line">2020-12-18 上映</p>
        </li>
        <li class="col2 tr">48524</li>
        <li class="col3 tr">38.620674</li>
        <li class="col4 tr">9</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246001'">
        <li class="col0">259</li>
        <li class="col1">
            <p class="first-line">小时代4：灵魂尽头</p>
            <p class="second-line">2015-07-09 上映</p>
        </li>
        <li class="col2 tr">48469</li>
        <li class="col3 tr">30.987238</li>
        <li class="col4 tr">33</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246210'">
        <li class="col0">260</li>
        <li class="col1">
            <p class="first-line">左耳</p>
            <p class="second-line">2015-04-24 上映</p>
        </li>
        <li class="col2 tr">48442</li>
        <li class="col3 tr">33.99673</li>
        <li class="col4 tr">25</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78051'">
        <li class="col0">261</li>
        <li class="col1">
            <p class="first-line">小时代</p>
            <p class="second-line">2013-06-27 上映</p>
        </li>
        <li class="col2 tr">48432</li>
        <li class="col3 tr">31.816536</li>
        <li class="col4 tr">32</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78589'">
        <li class="col0">262</li>
        <li class="col1">
            <p class="first-line">王牌特工：特工学院</p>
            <p class="second-line">2015-03-27 上映</p>
        </li>
        <li class="col2 tr">48367</li>
        <li class="col3 tr">33.911823</li>
        <li class="col4 tr">29</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341749'">
        <li class="col0">263</li>
        <li class="col1">
            <p class="first-line">我不是潘金莲</p>
            <p class="second-line">2016-11-18 上映</p>
        </li>
        <li class="col2 tr">48279</li>
        <li class="col3 tr">35.103405</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246388'">
        <li class="col0">264</li>
        <li class="col1">
            <p class="first-line">摆渡人</p>
            <p class="second-line">2016-12-23 上映</p>
        </li>
        <li class="col2 tr">48256</li>
        <li class="col3 tr">32.916817</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78611'">
        <li class="col0">265</li>
        <li class="col1">
            <p class="first-line">哥斯拉</p>
            <p class="second-line">2014-06-13 上映</p>
        </li>
        <li class="col2 tr">48125</li>
        <li class="col3 tr">38.12168</li>
        <li class="col4 tr">26</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1217637'">
        <li class="col0">266</li>
        <li class="col1">
            <p class="first-line">厉害了，我的国</p>
            <p class="second-line">2018-03-02 上映</p>
        </li>
        <li class="col2 tr">48059</li>
        <li class="col3 tr">31.555008</li>
        <li class="col4 tr">26</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1206605'">
        <li class="col0">267</li>
        <li class="col1">
            <p class="first-line">绿皮书</p>
            <p class="second-line">2019-03-01 上映</p>
        </li>
        <li class="col2 tr">47872</li>
        <li class="col3 tr">33.197285</li>
        <li class="col4 tr">13</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/247185'">
        <li class="col0">268</li>
        <li class="col1">
            <p class="first-line">星球大战外传：侠盗一号</p>
            <p class="second-line">2017-01-06 上映</p>
        </li>
        <li class="col2 tr">47719</li>
        <li class="col3 tr">36.65965</li>
        <li class="col4 tr">13</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/341173'">
        <li class="col0">269</li>
        <li class="col1">
            <p class="first-line">王牌特工2：黄金圈</p>
            <p class="second-line">2017-10-20 上映</p>
        </li>
        <li class="col2 tr">47428</li>
        <li class="col3 tr">35.414913</li>
        <li class="col4 tr">14</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/3'">
        <li class="col0">270</li>
        <li class="col1">
            <p class="first-line">非诚勿扰2</p>
            <p class="second-line">2010-12-22 上映</p>
        </li>
        <li class="col2 tr">47159</li>
        <li class="col3 tr">38.6498</li>
        <li class="col4 tr">44</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1235560'">
        <li class="col0">271</li>
        <li class="col1">
            <p class="first-line">白蛇：缘起</p>
            <p class="second-line">2019-01-11 上映</p>
        </li>
        <li class="col2 tr">46862</li>
        <li class="col3 tr">33.784885</li>
        <li class="col4 tr">10</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/451'">
        <li class="col0">272</li>
        <li class="col1">
            <p class="first-line">加勒比海盗4：惊涛怪浪</p>
            <p class="second-line">2011-05-20 上映</p>
        </li>
        <li class="col2 tr">46425</li>
        <li class="col3 tr">38.33827</li>
        <li class="col4 tr">45</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78435'">
        <li class="col0">273</li>
        <li class="col1">
            <p class="first-line">霍比特人2：史矛革之战</p>
            <p class="second-line">2014-02-21 上映</p>
        </li>
        <li class="col2 tr">46259</li>
        <li class="col3 tr">40.72935</li>
        <li class="col4 tr">26</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1412992'">
        <li class="col0">274</li>
        <li class="col1">
            <p class="first-line">李茂扮太子</p>
            <p class="second-line">2022-01-01 上映</p>
        </li>
        <li class="col2 tr">46242</li>
        <li class="col3 tr">39.03564</li>
        <li class="col4 tr">7</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1433776'">
        <li class="col0">275</li>
        <li class="col1">
            <p class="first-line">变形金刚：超能勇士崛起</p>
            <p class="second-line">2023-06-09 上映</p>
        </li>
        <li class="col2 tr">45940</li>
        <li class="col3 tr">37.762794</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1198177'">
        <li class="col0">276</li>
        <li class="col1">
            <p class="first-line">缝纫机乐队</p>
            <p class="second-line">2017-09-29 上映</p>
        </li>
        <li class="col2 tr">45936</li>
        <li class="col3 tr">32.841473</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1299124'">
        <li class="col0">277</li>
        <li class="col1">
            <p class="first-line">新神榜：哪吒重生</p>
            <p class="second-line">2021-02-12 上映</p>
        </li>
        <li class="col2 tr">45634</li>
        <li class="col3 tr">43.812588</li>
        <li class="col4 tr">14</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1297973'">
        <li class="col0">278</li>
        <li class="col1">
            <p class="first-line">信条</p>
            <p class="second-line">2020-09-04 上映</p>
        </li>
        <li class="col2 tr">45623</li>
        <li class="col3 tr">38.887432</li>
        <li class="col4 tr">10</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78653'">
        <li class="col0">279</li>
        <li class="col1">
            <p class="first-line">同桌的你</p>
            <p class="second-line">2014-04-25 上映</p>
        </li>
        <li class="col2 tr">45557</li>
        <li class="col3 tr">32.738598</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78488'">
        <li class="col0">280</li>
        <li class="col1">
            <p class="first-line">敢死队3</p>
            <p class="second-line">2014-09-01 上映</p>
        </li>
        <li class="col2 tr">45273</li>
        <li class="col3 tr">32.364616</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1229845'">
        <li class="col0">281</li>
        <li class="col1">
            <p class="first-line">晴雅集</p>
            <p class="second-line">2020-12-25 上映</p>
        </li>
        <li class="col2 tr">45142</li>
        <li class="col3 tr">37.490467</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/635'">
        <li class="col0">282</li>
        <li class="col1">
            <p class="first-line">冰川时代4</p>
            <p class="second-line">2012-07-27 上映</p>
        </li>
        <li class="col2 tr">44741</li>
        <li class="col3 tr">38.10555</li>
        <li class="col4 tr">28</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78637'">
        <li class="col0">283</li>
        <li class="col1">
            <p class="first-line">冰川时代5：星际碰撞</p>
            <p class="second-line">2016-08-23 上映</p>
        </li>
        <li class="col2 tr">44659</li>
        <li class="col3 tr">31.57359</li>
        <li class="col4 tr">15</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/249875'">
        <li class="col0">284</li>
        <li class="col1">
            <p class="first-line">谍影重重5</p>
            <p class="second-line">2016-08-23 上映</p>
        </li>
        <li class="col2 tr">44648</li>
        <li class="col3 tr">33.325996</li>
        <li class="col4 tr">16</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78425'">
        <li class="col0">285</li>
        <li class="col1">
            <p class="first-line">灰姑娘</p>
            <p class="second-line">2015-03-13 上映</p>
        </li>
        <li class="col2 tr">44397</li>
        <li class="col3 tr">31.517685</li>
        <li class="col4 tr">24</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1203575'">
        <li class="col0">286</li>
        <li class="col1">
            <p class="first-line">反贪风暴3</p>
            <p class="second-line">2018-09-14 上映</p>
        </li>
        <li class="col2 tr">44300</li>
        <li class="col3 tr">35.903458</li>
        <li class="col4 tr">10</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246316'">
        <li class="col0">287</li>
        <li class="col1">
            <p class="first-line">奔跑吧！兄弟</p>
            <p class="second-line">2015-01-30 上映</p>
        </li>
        <li class="col2 tr">44275</li>
        <li class="col3 tr">36.152008</li>
        <li class="col4 tr">26</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/246461'">
        <li class="col0">288</li>
        <li class="col1">
            <p class="first-line">星际迷航3：超越星辰</p>
            <p class="second-line">2016-09-02 上映</p>
        </li>
        <li class="col2 tr">44026</li>
        <li class="col3 tr">35.405113</li>
        <li class="col4 tr">14</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1356063'">
        <li class="col0">289</li>
        <li class="col1">
            <p class="first-line">峰爆</p>
            <p class="second-line">2021-09-17 上映</p>
        </li>
        <li class="col2 tr">43819</li>
        <li class="col3 tr">37.91477</li>
        <li class="col4 tr">8</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78361'">
        <li class="col0">290</li>
        <li class="col1">
            <p class="first-line">地心引力</p>
            <p class="second-line">2013-11-19 上映</p>
        </li>
        <li class="col2 tr">43549</li>
        <li class="col3 tr">41.292526</li>
        <li class="col4 tr">23</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/78684'">
        <li class="col0">291</li>
        <li class="col1">
            <p class="first-line">小黄人大眼萌</p>
            <p class="second-line">2015-09-13 上映</p>
        </li>
        <li class="col2 tr">43512</li>
        <li class="col3 tr">34.031704</li>
        <li class="col4 tr">20</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/338402'">
        <li class="col0">292</li>
        <li class="col1">
            <p class="first-line">全球风暴</p>
            <p class="second-line">2017-10-27 上映</p>
        </li>
        <li class="col2 tr">43403</li>
        <li class="col3 tr">34.574223</li>
        <li class="col4 tr">13</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1212303'">
        <li class="col0">293</li>
        <li class="col1">
            <p class="first-line">古董局中局</p>
            <p class="second-line">2021-12-03 上映</p>
        </li>
        <li class="col2 tr">42995</li>
        <li class="col3 tr">38.091557</li>
        <li class="col4 tr">6</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/1212512'">
        <li class="col0">294</li>
        <li class="col1">
            <p class="first-line">蜘蛛侠：平行宇宙</p>
            <p class="second-line">2018-12-21 上映</p>
        </li>
        <li class="col2 tr">42753</li>
        <li class="col3 tr">35.8091</li>
        <li class="col4 tr">13</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/338349'">
        <li class="col0">295</li>
        <li class="col1">
            <p class="first-line">血战钢锯岭</p>
            <p class="second-line">2016-12-08 上映</p>
        </li>
        <li class="col2 tr">42582</li>
        <li class="col3 tr">29.745615</li>
        <li class="col4 tr">19</li>
    </ul>
    <ul class="row" data-com="hrefTo,href:'/movie/789'">
        <li class="col0">296</li>
        <li class="col1">
            <p class="first-line">建国大业</p>
            <p class="second-line">2009-09-16 上映</p>
        </li>
        <li class="col2 tr">42018</li>
        <li class="col3 tr">32.42938</li>
        <li class="col4 tr">52</li>
    </ul>
</div>
<div data-com="gotoTop"></div>
<div style="width:100%;height:constant(safe-area-inset-bottom);height:env(safe-area-inset-bottom);"></div>
<script src="https://obj.pipi.cn/festatic/piaofang/common-config.js?v&#x3D;0.08309034287249495"></script>
<script crossorigin="anonymous" src="//www.dpfile.com/app/owl/static/owl_1.10.0.js"></script>
<script>
  window.owl('start', {
    
    project: 'movie-pro-nbox',
    resource: {
      enableStatusCheck: true,
    },
    resourceReg: /(.51ping|.dianping|.dpfile|.meituan|.sankuai|.kuxun|.maoyan|.neixin|.mobike|.dper.com|.pipi.cn)/,
    ajax: {
      invalid:false
    },
    error: {
      formatUnhandledRejection: true
    }
  });
</script>
<script>
  var isDev=false;
  var isTest=false;
  var __limitFeature = '';
  //bfcache
  window.addEventListener('pageshow',function (ev){
    if (ev.persisted) {
      window.location.reload();
    }
  });
  window.__pageScrollToTop = window.__pageScrollToTop || function() {};
</script>
<script type="text/javascript">
  !(function (win, doc, ns) {
    var cacheFunName = '_MeiTuanALogObject';
    win[cacheFunName] = ns;
    if (!win[ns]) {
      var _LX = function () {
        _LX.q.push(arguments);
        return _LX;
      };
      _LX.q = _LX.q || [];
      _LX.l = +new Date();
      win[ns] = _LX;
    }
  })(window, document, 'LXAnalytics');
</script>
<script src="//analytics.meituan.net/analytics.js" type="text/javascript" charset="utf-8" async defer></script>
<script>window._KNB_IGNORE_WECHAT=true;</script>
  <script src="//s0.meituan.net/bs/knb/v1.6.6/knb.js"></script>
<script>
  window.useKNB=true;
  window.felisConfig = {
    debug: false,
    combo: '//obj.pipi.cn/festatic/',
    comboPrefix: 'moviepro',
    contextPath: '/source',
    modules: [{"m":"/source/lib/zepto.js","s":31820,"v":"c479abb3"},{"m":"/source/util/env.js","s":2883,"v":"e76c4859"},{"m":"/source/util/msg/msg.js","s":4456,"v":"c540da3a"},{"m":"/source/util/tools.js","s":6649,"v":"e1890b60"},{"m":"/source/util/cookie.js","s":440,"v":"ebd8ee65"},{"m":"/source/util/nAjax.js","s":974,"v":"e044b9ab"},{"m":"/source/lib/count.js","s":6583,"v":"55b6f5c1"},{"m":"/source/util/analytics.js","s":20582,"v":"8e4d610b"},{"m":"/source/util/gaConfig.js","s":2080,"v":"d61fe519"},{"m":"/source/util/felis-coms.js","s":1510,"v":"55e37008"},{"m":"/source/util/hisBack.js","s":391,"v":"36e15d6c"},{"m":"/source/util/canTouch.js","s":389,"v":"160c8819"},{"m":"/source/util/gotoTop.js","s":365,"v":"c808c964"},{"m":"/source/util/hrefTo.js","s":460,"v":"0bfcd201"},{"m":"/source/biz/rankings.js","s":6635,"v":"7107ee88"}],
    loaded: function() {
      window.felisLoadedCallback && felisLoadedCallback();
    }
  };
</script>
<script src="//obj.pipi.cn/festatic/moviepro/common/felis-a12fe944.js"></script>
</body>
</html>

    """
    soup = BeautifulSoup(rsptext, 'html.parser')
    uls = soup.select("#ranks-list .row")
    for ul in uls:
        movieName = ul.select_one('.first-line').text
        releaseDate = ul.select_one('.second-line').text.removesuffix(" 上映")
        allMoney = int(ul.select_one('.col2').text)
        avgMoney = float(ul.select_one('.col3').text)
        avgPeople = int(ul.select_one('.col4').text)
        url = ul['data-com'].removeprefix("hrefTo,href:'").removesuffix("'")
        url = "https://piaofang.maoyan.com" + url + '/moresections'
        res = requests.get(url, cookies=cookies, headers=headers)
        res.encoding = res.apparent_encoding
        # 返回网页内容
        log.debug(res.json()['sectionHTMLs']['techSection']['html'])
        print()
