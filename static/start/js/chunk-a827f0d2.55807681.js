(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-a827f0d2"],{"2f25":function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"page-content"},[n("div",{staticClass:"news-block-wrapper page-block page-padding-y"},[n("h1",[t._v("Свежие новости")]),n("div",{staticClass:"news-block"},t._l(t.news,(function(e){return n("div",{key:e.id,staticClass:"news-item flex-between align-top"},[n("div",{staticClass:"text"},[n("h3",[t._v(t._s(e.title))]),n("p",[t._v(t._s(e.text))])]),n("div",{staticClass:"image"},[n("img",{attrs:{src:t.genImageUrl(e),alt:""}})])])})),0),n("div",{staticClass:"load-more"},[t._v("Ещё новости")])])])},r=[],s=(n("99af"),{name:"News",props:["news"],methods:{genImageUrl:function(t){return"".concat("http://188.120.245.208/").concat(t.image)}}}),i=s,c=n("2877"),o=Object(c["a"])(i,a,r,!1,null,"5931b84e",null);e["default"]=o.exports},"99af":function(t,e,n){"use strict";var a=n("23e7"),r=n("d039"),s=n("e8b5"),i=n("861d"),c=n("7b0b"),o=n("50c4"),l=n("8418"),d=n("65f0"),f=n("1dde"),u=n("b622"),p=n("2d00"),v=u("isConcatSpreadable"),w=9007199254740991,g="Maximum allowed index exceeded",b=p>=51||!r((function(){var t=[];return t[v]=!1,t.concat()[0]!==t})),h=f("concat"),m=function(t){if(!i(t))return!1;var e=t[v];return void 0!==e?!!e:s(t)},_=!b||!h;a({target:"Array",proto:!0,forced:_},{concat:function(t){var e,n,a,r,s,i=c(this),f=d(i,0),u=0;for(e=-1,a=arguments.length;e<a;e++)if(s=-1===e?i:arguments[e],m(s)){if(r=o(s.length),u+r>w)throw TypeError(g);for(n=0;n<r;n++,u++)n in s&&l(f,u,s[n])}else{if(u>=w)throw TypeError(g);l(f,u++,s)}return f.length=u,f}})}}]);
//# sourceMappingURL=chunk-a827f0d2.55807681.js.map