webpackJsonp([6],{"55Ec":function(e,t,r){"use strict";var l={render:function(){var e=this,t=e.$createElement,r=e._self._c||t;return r("div",{staticClass:"container _makedoc"},[r("el-form",{ref:"formdoc",staticClass:"demo-form-inline",attrs:{"label-position":e.labelPosition,"label-width":e.labelWidth,rules:e.rulesEdit,inline:!1,model:e.formdoc}},[r("el-form-item",{attrs:{label:"确认书网址",prop:"Controlurl"}},[r("el-input",{staticStyle:{width:"650px"},attrs:{type:"textarea",rows:3,placeholder:"确认书网址"},model:{value:e.formdoc.Controlurl,callback:function(t){e.$set(e.formdoc,"Controlurl",t)},expression:"formdoc.Controlurl"}})],1),e._v(" "),r("el-form-item",{attrs:{label:"检材编号",prop:"Sampleids"}},[r("el-input",{staticStyle:{width:"550px"},attrs:{type:"textarea",placeholder:"请输入检材编号，多个编号用 * 分割"},model:{value:e.formdoc.Sampleids,callback:function(t){e.$set(e.formdoc,"Sampleids",t)},expression:"formdoc.Sampleids"}}),e._v(">")],1),e._v(" "),r("el-form-item",{attrs:{label:"试剂类型",prop:"Reagent"}},[r("el-radio-group",{model:{value:e.formdoc.Reagent,callback:function(t){e.$set(e.formdoc,"Reagent",t)},expression:"formdoc.Reagent"}},[r("el-radio",{attrs:{label:0}},[e._v("GlobalFiler")]),e._v(" "),r("el-radio",{attrs:{label:1}},[e._v("PowerPlex®21")]),e._v(" "),r("el-radio",{attrs:{label:2}},[e._v("Identifiler Plus")])],1)],1),e._v(" "),r("el-form-item",{attrs:{label:"第一鉴定人",prop:"Firster"}},[r("el-radio-group",{model:{value:e.formdoc.Firster,callback:function(t){e.$set(e.formdoc,"Firster",t)},expression:"formdoc.Firster"}},[r("el-radio",{attrs:{label:0}},[e._v("LXY")]),e._v(" "),r("el-radio",{attrs:{label:1}},[e._v("LT")])],1)],1),e._v(" "),r("el-form-item",{staticStyle:{"margin-left":"0px"},attrs:{label:" "}},[r("el-button",{attrs:{type:"primary"},on:{click:e.onIdentity}},[e._v("生成鉴定书")]),e._v(" "),r("el-button",{attrs:{type:"primary"},on:{click:e.onReport}},[e._v("生成检验报告")])],1)],1)],1)},staticRenderFns:[]};t.a=l},Ekjn:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var l,o=r("qzrg");(l=o)&&l.__esModule;t.default={name:"makedoc",data:function(){return{formdoc:{Controlurl:"",Sampleids:"",Reagent:0,Firster:0},rulesEdit:{Controlurl:[{required:!0,message:"请输入确认书网址",trigger:"blur"}]},labelPosition:"right",labelWidth:"100px"}},computed:{},filters:{},mounted:function(){this.onIdentity(),this.onReport(),this.initCKEditor()},methods:{}}},pQmk:function(e,t){},xn5C:function(e,t,r){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var l=r("Ekjn"),o=r.n(l);for(var a in l)"default"!==a&&function(e){r.d(t,e,function(){return l[e]})}(a);var i=r("55Ec");var n=function(e){r("pQmk")},s=r("C7Lr")(o.a,i.a,!1,n,null,null);t.default=s.exports}});
//# sourceMappingURL=6.7ac03ee75e226dcdee54.js.map