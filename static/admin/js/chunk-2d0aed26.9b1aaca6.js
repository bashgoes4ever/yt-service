(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d0aed26"],{"0c63":function(t,e,a){"use strict";a.r(e);var n=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("v-container",[a("v-row",{staticClass:"mt-5",attrs:{justify:"center"}},[a("v-col",{attrs:{cols:"6"}},[a("h2",[t._v("Редактирование заказа")]),a("v-form",[a("v-text-field",{attrs:{disabled:"",label:"Название"},model:{value:t.name,callback:function(e){t.name=e},expression:"name"}}),a("v-text-field",{attrs:{disabled:"",label:"Пользователь"},model:{value:t.account,callback:function(e){t.account=e},expression:"account"}}),a("v-text-field",{attrs:{disabled:"",label:"Общая сумма заказа"},model:{value:t.total_price,callback:function(e){t.total_price=e},expression:"total_price"}}),a("v-select",{attrs:{items:t.plans,"item-text":"name","item-value":"id",label:"План",rules:[function(t){return!!t||"Обязательное поле"}]},model:{value:t.plan,callback:function(e){t.plan=e},expression:"plan"}}),a("v-text-field",{attrs:{label:"ID провадйера"},model:{value:t.provider_id,callback:function(e){t.provider_id=e},expression:"provider_id"}}),a("v-text-field",{attrs:{type:"number",label:"Количество",rules:[function(t){return!!t||"Обязательное поле"}],required:""},model:{value:t.amount,callback:function(e){t.amount=e},expression:"amount"}}),a("v-text-field",{attrs:{type:"number",label:"Остаток",rules:[function(t){return!!t||"Обязательное поле"}],required:""},model:{value:t.remains,callback:function(e){t.remains=e},expression:"remains"}}),a("v-text-field",{attrs:{type:"number",label:"Цена",rules:[function(t){return!!t||"Обязательное поле"}],required:""},model:{value:t.price,callback:function(e){t.price=e},expression:"price"}}),a("v-select",{attrs:{items:t.statuses,"item-text":"name","item-value":"id",label:"Статус"},model:{value:t.status,callback:function(e){t.status=e},expression:"status"}}),a("v-textarea",{attrs:{label:"Комментарий"},model:{value:t.comment,callback:function(e){t.comment=e},expression:"comment"}}),a("v-btn",{staticClass:"primary",attrs:{disabled:!t.amount||!t.remains},on:{click:t.submit}},[t._v(" Редактировать заказ ")])],1)],1)],1)],1)},r=[],s=(a("99af"),a("b0c0"),a("96cf"),a("1da1")),i=a("5530"),l=a("2f62"),c={name:"EditOrder",data:function(){return{account:null,isLoading:!1,search:null,plan:null,plans:[],amount:null,remains:null,provider_id:null,name:null,comment:null,status:null,statuses:[],price:null,total_price:null}},mounted:function(){this.getOrder(),this.getPlans(),this.getStatuses()},methods:Object(i["a"])(Object(i["a"])({},Object(l["b"])(["setAlert"])),{},{getPlans:function(){var t=this;return Object(s["a"])(regeneratorRuntime.mark((function e(){var a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,t.axios({url:"".concat("http://188.120.245.208/","api/v1/plans/"),method:"GET"});case 2:a=e.sent,t.plans=a.data;case 4:case"end":return e.stop()}}),e)})))()},getOrder:function(){var t=this;return Object(s["a"])(regeneratorRuntime.mark((function e(){var a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,t.axios({url:"".concat("http://188.120.245.208/","api/v1/orders/").concat(t.$route.params.id),method:"GET"});case 2:a=e.sent,t.account=a.data.user.email,t.plan=a.data.plan?a.data.plan.id:null,t.amount=a.data.amount,t.remains=a.data.remains,t.provider_id=a.data.provider_id,t.name=a.data.name,t.comment=a.data.comment,t.status=a.data.status.id,t.price=a.data.price,t.total_price=a.data.total_price;case 13:case"end":return e.stop()}}),e)})))()},getStatuses:function(){var t=this;return Object(s["a"])(regeneratorRuntime.mark((function e(){var a;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:return e.next=2,t.axios({url:"".concat("http://188.120.245.208/","api/v1/orders/statuses"),method:"GET"});case 2:a=e.sent,t.statuses=a.data;case 4:case"end":return e.stop()}}),e)})))()},submit:function(){var t=this,e={plan:this.plan,amount:this.amount,remains:this.remains};this.provider_id&&(e["provider_id"]=this.provider_id),this.comment&&(e["comment"]=this.comment),this.status&&(e["status"]=this.status),this.axios({url:"".concat("http://188.120.245.208/","api/v1/orders/").concat(this.$route.params.id),method:"PUT",data:e}).then((function(){t.setAlert({active:!0,color:"success",text:"Заказ создан"}),t.$router.push("/orders")})).catch((function(e){t.setAlert({active:!0,color:"error",text:e.response.data})}))}})},o=c,u=a("2877"),d=a("6544"),m=a.n(d),p=a("8336"),v=a("62ad"),f=a("a523"),b=a("4bd4"),h=a("0fd9"),x=a("b974"),_=a("8654"),k=a("a844"),w=Object(u["a"])(o,n,r,!1,null,"6d049d2c",null);e["default"]=w.exports;m()(w,{VBtn:p["a"],VCol:v["a"],VContainer:f["a"],VForm:b["a"],VRow:h["a"],VSelect:x["a"],VTextField:_["a"],VTextarea:k["a"]})}}]);
//# sourceMappingURL=chunk-2d0aed26.9b1aaca6.js.map