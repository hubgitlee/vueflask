<template>
    <div class="container _globalfiler">
        <!-- 查询区----start -->
        <el-form :label-position="labelPosition" :label-width="labelWidth" :inline="true" ref="formSearch" :model="formSearch" class="demo-form-inline">
            <el-form-item label="检材编号" prop="SampleID">
                <el-input v-model="formSearch.SampleID" placeholder="检材编号" style="width:200px;"></el-input>
            </el-form-item>
            <el-form-item label="添加时间" prop="add_time">
                <el-date-picker
                    v-model="formSearch.add_time"
                    type="daterange"
                    range-separator="至"
                    start-placeholder="开始日期"
                    end-placeholder="结束日期">
                </el-date-picker>
            </el-form-item>
            <el-form-item label=" " style="margin-left:0px;">
                <el-button type="primary" @click="onSearch">查询</el-button>
                <el-button type="warning" @click="onReset">重置</el-button>
            </el-form-item>
        </el-form>
        <!-- 查询区----end -->
        <!-- 操作区----start -->
        <el-row class="mgb15">
            <el-button size="small" round type="danger" @click="deleteMany">批量删除</el-button>
            <el-button size="small" round type="primary" @click="handleAdd"> 新 增 </el-button>
            <el-button size="small" round type="primary" @click="onOpenAdd">导入Codis文件
                
            </el-button>
        </el-row>
        <!-- 操作区----end -->
        <!-- 表格---start -->
        <el-table :data="tableData" v-loading="listLoading"  border stripe style="width: 100%" @selection-change="handleSelectionChange">
            <el-table-column type="selection" width="22">
            </el-table-column>
            <el-table-column prop="SampleID" label="检材编号" width="150" align="center" sortable>
                <!-- <template slot-scope="scope">
                    <a href="javacript:;" style="color: #00D1B2" @click="handleDetail(scope.$index, scope.row)">{{ scope.row.title}}</a>
                </template> -->
            </el-table-column>
            <el-table-column prop="D3S1358" label="D3S1358" align="center" width="80">
            </el-table-column>
            <el-table-column prop="vWA" label="vWA" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D16S539" label="D16S539" align="center" width="80">
            </el-table-column>
            <el-table-column prop="CSF1PO" label="CSF1PO" align="center" width="80">
            </el-table-column>
            <el-table-column prop="TPOX" label="TPOX" align="center" width="80">
            </el-table-column>
            <el-table-column prop="Yindel" label="Yindel" align="center" width="80">
            </el-table-column>
            <el-table-column prop="Amel" label="Amel" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D8S1179" label="D8S1179" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D21S11" label="D21S11" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D18S51" label="D18S51" align="center" width="80">
            </el-table-column>
            <el-table-column prop="DYS391" label="DYS391" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D2S441" label="D2S441" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D19S433" label="D19S433" align="center" width="80">
            </el-table-column>
            <el-table-column prop="TH01" label="TH01" align="center" width="80">
            </el-table-column>
            <el-table-column prop="FGA" label="FGA" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D22S1045" label="D22S1045" align="center" width="90">
            </el-table-column>
            <el-table-column prop="D5S818" label="D5S818" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D13S317" label="D13S317" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D7S820" label="D7S820" align="center" width="80">
            </el-table-column>
            <el-table-column prop="SE33" label="SE33" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D10S1248" label="D10S1248" align="center" width="90">
            </el-table-column>
            <el-table-column prop="D1S1656" label="D1S1656" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D12S391" label="D12S391" align="center" width="80">
            </el-table-column>
            <el-table-column prop="D2S1338" label="D2S1338" align="center" width="80">
            </el-table-column>
            <el-table-column prop="add_time" label="添加日期" align="center" :formatter="this.$common.timestampToTime" width="160" sortable>
            </el-table-column>
            <el-table-column label="操作" fixed="right" min-width="150">
                <template slot-scope="scope">                  
                    <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                    <el-button size="mini" plain type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
        <el-pagination background layout="total,sizes,prev, pager, next,jumper" :current-page="pageInfo.currentPage" :page-size="pageInfo.pageSize" :total="pageInfo.pageTotal" :page-sizes="[10,20,30,40,50]" @size-change="handleSizeChange" @current-change="handleCurrentChange">
        </el-pagination>
        <!-- 表格---end -->

        <!-- 编辑弹框---start -->
        <el-dialog  :title="formEditTitle" :visible.sync="dialogEdittVisible" width="700px" @close="closeDialog('formEdit')">
            <el-form :label-position="labelPosition" :label-width="labelWidth" :rules="rulesEdit" :disabled="formEditDisabled" :inline="true" ref="formEdit" :model="formEdit" class="demo-form-inline">
                <el-form-item prop="SampleID" label="检材编号">
                    <el-input v-model="formEdit.SampleID" placeholder="检材编号" style="width:200px;"></el-input>
                </el-form-item>
                <el-form-item prop="D3S1358" label="D3S1358">
                    <el-input v-model="formEdit.D3S1358"></el-input>
                </el-form-item>
                <el-form-item prop="vWA" label="vWA">
                    <el-input v-model="formEdit.vWA"></el-input>
                </el-form-item>
                <el-form-item prop="D16S539" label="D16S539">
                    <el-input v-model="formEdit.D16S539"></el-input>
                </el-form-item>
                <el-form-item prop="CSF1PO" label="CSF1PO">
                    <el-input v-model="formEdit.CSF1PO"></el-input>
                </el-form-item>
                <el-form-item prop="TPOX" label="TPOX">
                    <el-input v-model="formEdit.TPOX"></el-input>
                </el-form-item>
                <el-form-item prop="Yindel" label="Yindel">
                    <el-input v-model="formEdit.Yindel"></el-input>
                </el-form-item>
                <el-form-item prop="Amel" label="Amel">
                    <el-input v-model="formEdit.Amel"></el-input>
                </el-form-item>
                <el-form-item prop="D8S1179" label="D8S1179">
                    <el-input v-model="formEdit.D8S1179"></el-input>
                </el-form-item>
                <el-form-item prop="D21S11" label="D21S11">
                    <el-input v-model="formEdit.D21S11"></el-input>
                </el-form-item>
                <el-form-item prop="D18S51" label="D18S51">
                    <el-input v-model="formEdit.D18S51"></el-input>
                </el-form-item>
                <el-form-item prop="DYS391" label="DYS391">
                    <el-input v-model="formEdit.DYS391"></el-input>
                </el-form-item>
                <el-form-item prop="D2S441" label="D2S441">
                    <el-input v-model="formEdit.D2S441"></el-input>
                </el-form-item>
                <el-form-item prop="D19S433" label="D19S433">
                    <el-input v-model="formEdit.D19S433"></el-input>
                </el-form-item>
                <el-form-item prop="TH01" label="TH01">
                    <el-input v-model="formEdit.TH01"></el-input>
                </el-form-item>
                <el-form-item prop="FGA" label="FGA">
                    <el-input v-model="formEdit.FGA"></el-input>
                </el-form-item>
                <el-form-item prop="D22S1045" label="D22S1045">
                    <el-input v-model="formEdit.D22S1045"></el-input>
                </el-form-item>
                <el-form-item prop="D5S818" label="D5S818">
                    <el-input v-model="formEdit.D5S818"></el-input>
                </el-form-item>
                <el-form-item prop="D13S317" label="D13S317">
                    <el-input v-model="formEdit.D13S317"></el-input>
                </el-form-item>
                <el-form-item prop="D7S820" label="D7S820">
                    <el-input v-model="formEdit.D7S820"></el-input>
                </el-form-item>
                <el-form-item prop="SE33" label="SE33">
                    <el-input v-model="formEdit.SE33"></el-input>
                </el-form-item>
                <el-form-item prop="D10S1248" label="D10S1248">
                    <el-input v-model="formEdit.D10S1248"></el-input>
                </el-form-item>
                <el-form-item prop="D1S1656" label="D1S1656">
                    <el-input v-model="formEdit.D1S1656"></el-input>
                </el-form-item>
                <el-form-item prop="D12S391" label="D12S391">
                    <el-input v-model="formEdit.D12S391"></el-input>
                </el-form-item>
                <el-form-item prop="D2S1338" label="D2S1338">
                    <el-input v-model="formEdit.D2S1338"></el-input>
                </el-form-item>     
            </el-form>

            <div slot="footer" class="dialog-footer">
                <el-button @click="dialogEdittVisible = false">取 消</el-button>
                <el-button v-if="!formEditDisabled" type="primary" @click="handleSave">确 定</el-button>
            </div>
        </el-dialog>

        <!-- 编辑弹框---end -->  

        <!-- codis导入弹框---start -->
        <el-dialog  :title="codisEditTitle" :visible.sync="codisEdittVisible" width="550px" @close="closeCodis('formEdit')">
            <el-form label-position="right" label-width="100px" :rules="codisrulesEdit" :disabled="codisEditDisabled" :inline="false" ref="formEdit" :model="formEdit" class="demo-form-inline">
                <el-form-item  label="导入文件">
                    <el-button  size="small" type="primary" >codis文件导入
                        <input type="file" style="opacity:0;width:80px;height:100%;position:absolute;top:0;left:0;cursor:pointer;" @change="getFile($event)">
                    </el-button>
                    <span :class="{ 'el-icon-success': this.file, 'el-icon-warning': !this.file}">{{this.file?'已上传':'未上传'}}</span>
                </el-form-item>
                <el-form-item label="文件名称" prop="name">
                    <el-input v-model="formEdit.name" placeholder="文件名称" ></el-input>
                </el-form-item>
                <el-form-item label="文件类型" prop="type">
                    <el-input placeholder="文件类型" ></el-input>
                </el-form-item>
            </el-form>

            <div slot="footer" class="dialog-footer">
                <el-button @click="codisEdittVisible = false">取 消</el-button>
                <el-button v-if="!codisEditDisabled" type="primary" @click="onSave($event)">Codis导入</el-button>
            </div>
        </el-dialog>

        <!-- codis导入弹框---end -->

    </div>
</template>

<style lang="scss">
// 设置输入框的宽度
._globalfiler{
    .el-input {
        width: 110px;
    }
    // 关键字 start
     .el-tag {
        margin-right: 10px;
    }
    .button-new-tag {
        // margin-left: 10px;
        height: 32px;
        line-height: 30px;
        padding-top: 0;
        padding-bottom: 0;
    }
    .input-new-tag {
        width: 90px;
        // margin-left: 10px;
        vertical-align: bottom;
    }
    // 关键字 end
    ._edit{
        .docTitle{
            width:439px;
        }
        ._editor{
            width:100%;
            .el-form-item__content{
                width:100%;
                .document-editor{
                    border:1px solid #c4c4c4;
                    .document-editor__toolbar{
                        border:0;
                        border-bottom:1px solid #c4c4c4;
                        .ck-toolbar{
                            border:0;
                        }
                    }
                    .document-editor__editable{
                        min-height: 400px;
                        border:0;
                    }
                }
                
            }
            
        }
    }
    
}

</style>

<script>
import apis from '../../apis/apis';
// import DecoupledEditor from '@ckeditor/ckeditor5-build-decoupled-document';//文档模式
export default {
    name: 'globalfiler',
    data() {
        return {
            listLoading : false,//
            pageInfo: { //分页
                currentPage: 1,
                pageSize: 10,
                pageTotal: 80
            },
            formSearch: { //表单查询
                SampleID:'',
                createStartDate:null,//创建开始时间
                createEndDate:null,//创建结束时间
                add_time:null,
            },
            formEdit: { //表单新增,编辑,查看
                SampleID:'',
                D3S1358:'',
                vWA:'',
                D16S539:'',
                CSF1PO:'',
                TPOX:'',
                Yindel:'',
                Amel:'',
                D8S1179:'',
                D21S11:'',
                D18S51:'',
                DYS391:'',
                D2S441:'',
                D19S433:'',
                TH01:'',
                FGA:'',
                D22S1045:'',
                D5S818:'',
                D13S317:'',
                D7S820:'',
                SE33:'',
                D10S1248:'',
                D1S1656:'',
                D12S391:'',
                D2S1338:'',
            },
            rulesEdit:  {
                SampleID: [
                    { required: true, message: "请输入检材编号", trigger: "blur" },
                    { min: 2, max: 50, message: "长度在 2 到 50 个字符", trigger: "blur" }
                ],
            },
            formEditTitle:'编辑',//新增，编辑和查看标题
            formEditDisabled:false,//编辑弹窗是否可编辑
            dialogEdittVisible: false,  //编辑弹框显示
            dialogType:'',//弹框类型：add,edit,show
            tableData: [  //表单列表
                {   id:'',
                    SampleID:'',
                    D3S1358:'',
                    vWA:'',
                    D16S539:'',
                    CSF1PO:'',
                    TPOX:'',
                    Yindel:'',
                    Amel:'',
                    D8S1179:'',
                    D21S11:'',
                    D18S51:'',
                    DYS391:'',
                    D2S441:'',
                    D19S433:'',
                    TH01:'',
                    FGA:'',
                    D22S1045:'',
                    D5S818:'',
                    D13S317:'',
                    D7S820:'',
                    SE33:'',
                    D10S1248:'',
                    D1S1656:'',
                    D12S391:'',
                    D2S1338:'',
                    add_time:null, 
                }
            ],
            labelPosition: 'right', //lable对齐方式
            labelWidth: '80px', //lable宽度
            formLabelWidth: '120px',
            multipleSelection: [],
            isTableShow:true,//表格显示
            isEditShow:false,//编辑区显示
            editBtnText:'保存',//编辑按钮文本
            //关键字相关 start
            
            inputVisible: false,
            inputValue: '',
            //关键字相关 end
            //
            codisEditTitle:'codis导入',
            codisEditDisabled:false,//编辑弹窗是否可编辑
            codisEdittVisible: false,  //编辑弹框显示
            codisrulesEdit:{
                type: [
                    {trigger: "change" }
                    ]
            }
        };
    },
    computed:{     
    },
    filters: {
        convertPublic: function (state) {
            if(state=='未发布'){
                return '执行发布';
            }
            else if(state=='已发布')
            {
                return '取消发布';
            }
            else{
                return '执行发布';
            }
        },
        convertContent:(content)=>{
            if(content){
                return content.replace(/<[^>]*>/ig,"").replace(/\&nbsp;/g,""); 
            }
            else{
                return "";
            }
            
        },
        convertKeyWords:(keywords)=>{
            if(keywords&&keywords.length>0){
                return keywords.join(',');
            }
            else {
                return "";
            }
            
        },
    },
    mounted(){
        //todo:开发用
        //this.openEdit();

        this.onSearch();
        this.initCKEditor()
    },
    methods: {
        /**
         * 查询列表
         */
        onSearch(){
            this.listLoading=true;
        
            if(this.formSearch.add_time){
                this.formSearch.createStartDate=this.formSearch.add_time[0];
                this.formSearch.createEndDate=this.formSearch.add_time[1];
            }
            let param = Object.assign({}, this.formSearch,this.pageInfo);
            apis.globalfilerApi.getList(param)
            .then((data)=>{
                console.log(data);
                // console.log(JSON.stringify(data));
                this.listLoading=false;
                if (data && data.data) {
                        var json = data.data;
                        if (json.status == 'SUCCESS') {
                            this.pageInfo.pageTotal=json.count;
                            this.tableData=json.data;
                        }
                        else if (json.message) {
                            this.$message({message: json.message,type: "error"});
                        }
                }
            })
            .catch((err)=>{
                this.listLoading=false;
                this.$message({message: '查询异常，请重试',type: "error"});
            });
        },
        /**
         * 点击保存按钮
         */
        handleSave(){
            if(this.dialogType=='add'){
                this.save();
            }
            else if(this.dialogType=='edit'){
                this.update();
            }
            else{
                this.$message({message: '操作异常',type: "error"});
            }
        },
        /**
         * 保存
         */
        save() {
            this.$refs["formEdit"].validate(valid => {
                if(valid){
                    let param = Object.assign({}, this.formEdit);
                    // console.log(param)
                    // param.content=this.EditorObj.getData();
                    apis.globalfilerApi.add(param)
                    .then((data)=>{
                        console.log(data);
                        if(data&&data.data){
                            var json=data.data;
                            console.log("000");
                            // console.log(JSON.stringify(json));
                            if(json&&json.status=='SUCCESS'){
                                this.$message({message: '执行成功',type: "success"});
                                this.dialogEdittVisible = false;
                                // this.closeEdit();
                                this.onSearch();
                                return;
                            }
                        }
                        this.$message({message: '执行失败，请重试',type: "error"});
                    })
                    .catch((err)=>{
                        this.$message({message: '执行失败，请重试',type: "error"});
                    });
                } 
            });
        },
        /**
         * 打开codis弹框
         */
        onOpenAdd(){
          this.codisEdittVisible = true;
        },
        /**
         * 关闭codis弹框，数据重置
         */
        closeCodis(formName){
            this.$refs[formName].resetFields();
        },
        /**
         * 导入codis文件
         */
        getFile: function (event) {
        
          this.file = event.target.files[0];
          event.target.value="";
          if(this.file){
            this.formEdit.name=this.file.name;
          }
          else{
            this.formEdit.name='';
          }
          
          console.log(this.file);
        },
        onSave(event){

        },
         /**
         * 更新
         */
        update() {
            this.$refs["formEdit"].validate(valid => {
                if(valid){
                   
                    let param = Object.assign({}, this.formEdit);
                    param.content=this.EditorObj.getData();
                    apis.kbmsApi.update(param)
                    .then((data)=>{
                        if(data&&data.data){
                            var json=data.data;
                             if(json&&json.status=='SUCCESS'){
                                this.$message({message: '执行成功',type: "success"});
                                this.closeEdit();
                                this.onSearch();
                                return;
                            }
                        }
                       this.$message({message: '执行失败，请重试',type: "error"});
                    })
                    .catch((err)=>{
                        this.$message({message: '执行失败，请重试',type: "error"});
                    });
                }
                
                
            });
        },
         /**
         * 删除
         */
        handleDelete(index, rowData) {
            var id=rowData.id;
            this.$confirm('此操作将永久删除该文件, 是否继续?', '提示', {
                confirmButtonText: '确定',
                cancelButtonText: '取消',
                type: 'warning'
            }).then(() => {
                    apis.globalfilerApi.delete({id:id})
                    .then((data)=>{
                        this.$common.isSuccess(data,()=>{
                            debugger;
                            this.onSearch();
                        });
                    })
                    .catch((err)=>{
                        debugger;
                        this.$message({message: '执行失败，请重试',type: "error"});
                    });
                
            }).catch(() => {
                this.$message({type: 'info',message: '已取消删除'});
            });

        },
        /**
         * 批量删除
         */
        deleteMany() {
            var ids= this.multipleSelection.map(item => item.id);
            if(ids.length==0){
                 this.$message({message: '请选择要删除的项',type: "warn"});
                return;
            }
    
            this.$confirm('此操作将批量永久删除文件, 是否继续?', '提示', {
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                        apis.kbmsApi.deleteBatch({ids:ids})
                        .then((data)=>{
                            this.$common.isSuccess(data,()=>{
                                debugger;
                                this.onSearch();
                            });
                        })
                        .catch((err)=>{
                            debugger;
                            this.$message({message: '执行失败，请重试',type: "error"});
                        });
                    
                }).catch(() => {
                    this.$message({type: 'info',message: '已取消删除'});
                });

        },
        handlePublic(){
            debugger;
            this.formEdit.publicState='已发布';
            if(this.dialogType=='add'){
                this.save();
            }
            else if(this.dialogType=='edit'){
                this.update();
            }
            else{
                this.$message({message: '操作异常',type: "error"});
            }
        },
        //更新发布状态
        // updatePublicState(index, rowData,publicState){
        //     debugger;
        //     var id=rowData.id;
        //     var msg=publicState=='已发布'?'发布成功':'取消发布成功';
        //     apis.kbmsApi.updatePublicState({id:id,publicState:publicState})
        //                 .then((data)=>{
        //                     this.$common.isSuccess(data,()=>{
        //                         this.$message({type: 'success',message: msg});
        //                         this.onSearch();
        //                     });
        //                 })
        //                 .catch((err)=>{
        //                     this.$message({message: '执行失败，请重试',type: "error"});
        //                 });
        // },
        onReset(){
            this.$refs['formSearch'].resetFields();
        },
        /**
         * 打开新增页
         */
        handleAdd() {
            this.dialogEdittVisible = true;
            this.$nextTick(()=>{
                this.dialogType='add';
                this.formEditTitle='新增';
                this.formEditDisabled=false;
            });
        },
        /**
         * 打开编辑页
         */
        handleEdit(index, rowData) {
            this.openEdit();
            this.$nextTick(()=>{
                this.dialogType='edit';
                this.formEditTitle='编辑';
                this.editBtnText='保存修改';
                this.formEditDisabled=false;
                this.formEdit= Object.assign({}, rowData);
                this.EditorObj.setData(this.formEdit.content==null?'':this.formEdit.content);
                this.EditorObj.isReadOnly=false;
            });
            
        },
        /**
         * 打开详情页
         */
        handleDetail(index,rowData){
            //debugger;
            this.openEdit();
            this.$nextTick(()=>{
                this.dialogType='show';
                this.formEditTitle='详情';
                this.formEditDisabled=true;
                this.formEdit= Object.assign({}, rowData) ;
                this.EditorObj.setData(this.formEdit.content==null?'':this.formEdit.content);
                
                this.EditorObj.isReadOnly=true;
            });
        },
        /**
         * 关闭弹框，数据重置
         */
        closeDialog(formName){
            this.$refs[formName].resetFields();
        },
        /**
         * 分页大小切换
         */
        handleSizeChange(val) {
            this.pageInfo.pageSize = val;
            this.onSearch();
        },
        /**
         * 分页切换
         */
        handleCurrentChange(val) {
            this.pageInfo.currentPage = val;
            this.onSearch();
        },
        /**
         * 点击选择
         */
        handleSelectionChange(val) {
            this.multipleSelection = val;
            // this.$message({
            //     message: '选中的项是:' + JSON.stringify(this.multipleSelection),
            //     type: "success"
            // });
        },
        /**
         * 打开详情页
         */
        openDetail(row){
            this.$common.OpenNewPage(this,'detail',row);
        },
        /** 
         * 打开编辑页
         */
        openEdit(){
            this.isTableShow=false;
            this.isEditShow = true;
            // this.$nextTick(()=>{
            //     this.initCKEditor()
            // });
        },
         /** 
         * 关闭编辑页
         */
        closeEdit(){
            this.$refs['formEdit'].resetFields();
            this.isTableShow=true;
            this.isEditShow = false;
            
        },
         //初始化容器
        initCKEditor() {
            DecoupledEditor.create(document.querySelector('.document-editor__editable'), {
                ckfinder: {
                    // Upload the images to the server using the CKFinder QuickUpload command.
                    uploadUrl: '/api/img-api/upload'
                }
            })
            .then(editor => {
                    const toolbarContainer = document.querySelector('.document-editor__toolbar');
                    toolbarContainer.appendChild(editor.ui.view.toolbar.element);//添加工具栏
                    this.EditorObj = editor;
                    console.log('初始化富编辑器');
            })
            .catch(err => {
                    console.error(err);
                    console.log('初始化富编辑器失败');
            });
        }   
    }
};
</script>
