webpackJsonp([17],{"6PF9":function(e,t){},uJSN:function(e,t,a){"use strict";var i={render:function(){var e=this,t=e.$createElement,a=e._self._c||t;return a("div",{staticClass:"table"},[a("div",{staticClass:"crumbs"},[a("el-breadcrumb",{attrs:{separator:"/"}},[a("el-breadcrumb-item",[a("i",{staticClass:"el-icon-tickets"}),e._v("机构管理")])],1)],1),e._v(" "),a("div",{staticClass:"container"},[a("div",{staticClass:"custom-tree-container"},[a("div",{staticClass:"block"},[a("el-tree",{directives:[{name:"loading",rawName:"v-loading",value:e.listLoading,expression:"listLoading"}],attrs:{data:e.treeData,props:e.defaultProps,"node-key":"id","expand-on-click-node":!1},scopedSlots:e._u([{key:"default",fn:function(t){var i=t.node,o=t.data;return a("span",{staticClass:"custom-tree-node"},[a("span",[e._v(e._s(i.label)+"                           \n                          "),a("i",{staticClass:"el-icon-plus",on:{click:function(){return e.append(i,"1")}}}),e._v(" "),a("i",{staticClass:"el-icon-edit-outline",on:{click:function(){return e.append(i,"2")}}}),e._v(" "),a("i",{staticClass:"el-icon-delete",on:{click:function(){return e.remove(i,o)}}})])])}}])})],1)]),e._v(" "),a("el-dialog",{attrs:{title:"新增",visible:e.addFormVisible,"close-on-click-modal":!1},on:{"update:visible":function(t){e.addFormVisible=t}}},[a("el-form",{ref:"addForm",attrs:{model:e.addForm,"label-width":"80px",rules:e.formRules}},[a("el-form-item",{attrs:{label:"机构名称",prop:"orgName"}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.addForm.orgName,callback:function(t){e.$set(e.addForm,"orgName",t)},expression:"addForm.orgName"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"组织类型",prop:"orgType"}},[a("el-select",{attrs:{placeholder:"请选择"},model:{value:e.addForm.orgType,callback:function(t){e.$set(e.addForm,"orgType",t)},expression:"addForm.orgType"}},e._l(e.orgTypeOptions,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1)],1),e._v(" "),a("el-form-item",{attrs:{label:"是否有效",prop:"validateState"}},[a("el-select",{attrs:{placeholder:"请选择"},model:{value:e.addForm.validateState,callback:function(t){e.$set(e.addForm,"validateState",t)},expression:"addForm.validateState"}},e._l(e.validateStateOptions,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1)],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.addFormVisible=!1}}},[e._v("取消")]),e._v(" "),a("el-button",{attrs:{type:"primary",loading:e.addLoading},on:{click:e.addSubmit}},[e._v("提交")])],1)],1),e._v(" "),a("el-dialog",{attrs:{title:"编辑",visible:e.editFormVisible,"close-on-click-modal":!1},on:{"update:visible":function(t){e.editFormVisible=t}}},[a("el-form",{ref:"editForm",attrs:{model:e.editForm,"label-width":"80px",rules:e.formRules}},[a("el-form-item",{attrs:{label:"机构名称",prop:"orgName"}},[a("el-input",{attrs:{"auto-complete":"off"},model:{value:e.editForm.orgName,callback:function(t){e.$set(e.editForm,"orgName",t)},expression:"editForm.orgName"}})],1),e._v(" "),a("el-form-item",{attrs:{label:"组织类型",prop:"orgType"}},[a("el-select",{attrs:{placeholder:"请选择"},model:{value:e.editForm.orgType,callback:function(t){e.$set(e.editForm,"orgType",t)},expression:"editForm.orgType"}},e._l(e.orgTypeOptions,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1)],1),e._v(" "),a("el-form-item",{attrs:{label:"是否有效",prop:"validateState"}},[a("el-select",{attrs:{placeholder:"请选择"},model:{value:e.editForm.validateState,callback:function(t){e.$set(e.editForm,"validateState",t)},expression:"editForm.validateState"}},e._l(e.validateStateOptions,function(e){return a("el-option",{key:e.value,attrs:{label:e.label,value:e.value}})}),1)],1)],1),e._v(" "),a("div",{staticClass:"dialog-footer",attrs:{slot:"footer"},slot:"footer"},[a("el-button",{on:{click:function(t){e.editFormVisible=!1}}},[e._v("取消")]),e._v(" "),a("el-button",{attrs:{type:"primary",loading:e.editLoading},on:{click:e.editSubmit}},[e._v("提交")])],1)],1)],1)])},staticRenderFns:[]};t.a=i},x1QS:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var i=a("y88E"),o=a.n(i);for(var r in i)"default"!==r&&function(e){a.d(t,e,function(){return i[e]})}(r);var l=a("uJSN");var d=function(e){a("6PF9")},s=a("C7Lr")(o.a,l.a,!1,d,null,null);t.default=s.exports},y88E:function(e,t,a){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var i,o=a("aA9S"),r=(i=o)&&i.__esModule?i:{default:i};t.default={name:"OrganizationTree",data:function(){return{treeData:[],defaultProps:{children:"children",label:"name"},listLoading:!1,addFormVisible:!1,addLoading:!1,orgTypeOptions:[{value:"org",label:"组织"},{value:"dept",label:"部门"},{value:"store",label:"门店"}],validateStateOptions:[{value:"0",label:"无效"},{value:"1",label:"有效"}],formRules:{orgName:[{required:!0,message:"请输入机构名称",trigger:"blur"}],orgType:[{required:!0,message:"请选择组织类型",trigger:"blur"}],validateState:[{required:!0,message:"请选择是否有效",trigger:"blur"}]},addForm:{id:"",orgName:"",orgType:"",validateState:"",parentId:""},editFormVisible:!1,editLoading:!1,editForm:{id:"",orgName:"",orgType:"",validateState:"",parentId:""}}},methods:{getResult:function(){var e=this;this.listLoading=!0;var t=(0,r.default)({},{});this.$ajax({method:"post",url:"/api/sysorg-api/querySysOrgList",data:t}).then(function(t){e.treeData=t.data.data,e.listLoading=!1},function(t){e.treeData.message="Local Reeuest Error!"})},append:function(e,t){"1"==t&&(this.addForm.parentId=e.data.id,this.addForm.id="0",this.addFormVisible=!0),"2"==t&&(this.editFormVisible=!0,this.editForm.id=e.data.id,this.editForm.orgName=e.data.name,this.editForm.orgType=e.data.orgType,this.editForm.validateState=e.data.validateState,this.editForm.parentId=e.data.parentId)},remove:function(e,t){var a=this;this.$confirm("确认删除该记录吗?","提示",{type:"warning"}).then(function(){var i=new URLSearchParams;i.append("orgid",e.data.id),a.$ajax({method:"post",url:"/api/sysorg-api/deleteSysOrg",data:i}).then(function(i){a.$message({message:"删除成功",type:"success"});var o=e.parent,r=o.data.children||o.data,l=r.findIndex(function(e){return e.id===t.id});r.splice(l,1)})}).catch(function(){})},addSubmit:function(){var e=this;this.$refs.addForm.validate(function(t){t&&e.$confirm("确认提交吗？","提示",{}).then(function(){e.addLoading=!0;var t=(0,r.default)({},e.addForm);e.$ajax({method:"post",url:"/api/sysorg-api/addOrg",data:t}).then(function(t){e.addLoading=!1,e.$message({message:"提交成功",type:"success"}),e.$refs.addForm.resetFields(),e.addFormVisible=!1,e.getResult()})})})},editSubmit:function(){var e=this;this.$refs.editForm.validate(function(t){t&&e.$confirm("确认提交吗？","提示",{}).then(function(){e.editLoading=!0;var t=(0,r.default)({},e.editForm);e.$ajax({method:"post",url:"/api/sysorg-api/addOrg",data:t}).then(function(t){e.editLoading=!1,e.$message({message:"提交成功",type:"success"}),e.$refs.editForm.resetFields(),e.editFormVisible=!1,e.getResult()})})})}},mounted:function(){this.getResult()}}}});
//# sourceMappingURL=17.fd860ede41aadf26d03e.js.map