(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-58e6e451"],{"083a":function(t,e,i){"use strict";i.r(e);var r=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("v-container",[i("v-row",{staticClass:"mt-5",attrs:{justify:"center"}},[i("v-col",{attrs:{cols:"6"}},[i("h2",[t._v("Создание плана")]),i("v-form",[i("v-text-field",{attrs:{label:"Название",rules:[function(t){return!!t||"Обязательное поле"}],required:""},model:{value:t.name,callback:function(e){t.name=e},expression:"name"}}),i("v-text-field",{attrs:{label:"Стоимость",type:"number",rules:[function(t){return!!t||"Обязательное поле"}],required:""},model:{value:t.price,callback:function(e){t.price=e},expression:"price"}}),i("v-text-field",{attrs:{label:"ID провайдера"},model:{value:t.provider_id,callback:function(e){t.provider_id=e},expression:"provider_id"}}),i("v-btn",{staticClass:"primary",attrs:{disabled:!t.name||!t.price},on:{click:t.submit}},[t._v(" Создать план ")])],1)],1)],1)],1)},n=[],a=(i("b0c0"),i("5530")),s=i("2f62"),o={name:"AddPlan",data:function(){return{name:null,price:null,provider_id:null}},methods:Object(a["a"])(Object(a["a"])({},Object(s["b"])(["setAlert"])),{},{submit:function(){var t=this;this.axios({url:"".concat("http://188.120.245.208/","api/v1/plans/"),method:"POST",data:{name:this.name,price:this.price,provider_id:this.provider_id}}).then((function(){t.setAlert({active:!0,color:"success",text:"План создан"}),t.$router.push("/plans")})).catch((function(e){t.setAlert({active:!0,color:"error",text:e.response.data})}))}})},u=o,c=i("2877"),l=i("6544"),d=i.n(l),h=i("8336"),f=i("62ad"),p=i("a523"),v=i("4bd4"),m=i("0fd9"),b=i("8654"),_=Object(c["a"])(u,r,n,!1,null,"6db4c169",null);e["default"]=_.exports;d()(_,{VBtn:h["a"],VCol:f["a"],VContainer:p["a"],VForm:v["a"],VRow:m["a"],VTextField:b["a"]})},"4bd4":function(t,e,i){"use strict";i("4de4"),i("7db0"),i("4160"),i("caad"),i("07ac"),i("2532"),i("159b");var r=i("5530"),n=i("58df"),a=i("7e2b"),s=i("3206");e["a"]=Object(n["a"])(a["a"],Object(s["b"])("form")).extend({name:"v-form",provide:function(){return{form:this}},inheritAttrs:!1,props:{disabled:Boolean,lazyValidation:Boolean,readonly:Boolean,value:Boolean},data:function(){return{inputs:[],watchers:[],errorBag:{}}},watch:{errorBag:{handler:function(t){var e=Object.values(t).includes(!0);this.$emit("input",!e)},deep:!0,immediate:!0}},methods:{watchInput:function(t){var e=this,i=function(t){return t.$watch("hasError",(function(i){e.$set(e.errorBag,t._uid,i)}),{immediate:!0})},r={_uid:t._uid,valid:function(){},shouldValidate:function(){}};return this.lazyValidation?r.shouldValidate=t.$watch("shouldValidate",(function(n){n&&(e.errorBag.hasOwnProperty(t._uid)||(r.valid=i(t)))})):r.valid=i(t),r},validate:function(){return 0===this.inputs.filter((function(t){return!t.validate(!0)})).length},reset:function(){this.inputs.forEach((function(t){return t.reset()})),this.resetErrorBag()},resetErrorBag:function(){var t=this;this.lazyValidation&&setTimeout((function(){t.errorBag={}}),0)},resetValidation:function(){this.inputs.forEach((function(t){return t.resetValidation()})),this.resetErrorBag()},register:function(t){this.inputs.push(t),this.watchers.push(this.watchInput(t))},unregister:function(t){var e=this.inputs.find((function(e){return e._uid===t._uid}));if(e){var i=this.watchers.find((function(t){return t._uid===e._uid}));i&&(i.valid(),i.shouldValidate()),this.watchers=this.watchers.filter((function(t){return t._uid!==e._uid})),this.inputs=this.inputs.filter((function(t){return t._uid!==e._uid})),this.$delete(this.errorBag,e._uid)}}},render:function(t){var e=this;return t("form",{staticClass:"v-form",attrs:Object(r["a"])({novalidate:!0},this.attrs$),on:{submit:function(t){return e.$emit("submit",t)}}},this.$slots.default)}})}}]);
//# sourceMappingURL=chunk-58e6e451.1e043293.js.map