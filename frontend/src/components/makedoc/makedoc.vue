<template>
    <div class="container _makedoc">
        <!-- 查询区----start -->
        <el-form :label-position="labelPosition" :label-width="labelWidth" :rules="rulesEdit" :inline="false" ref="formdoc" :model="formdoc" class="demo-form-inline">
            <el-form-item label="确认书网址" prop="Controlurl">
                <el-input type="textarea" :rows="3" v-model="formdoc.Controlurl" placeholder="确认书网址" style="width:700px;"></el-input>
            </el-form-item>
            <el-form-item label="检材编号" prop="Sampleids">
                <el-input type="textarea" v-model="formdoc.Sampleids" placeholder="请输入检材编号，多个编号用 * 分割" style="width:550px;"></el-input>
            </el-form-item>
            <el-form-item label="试剂类型" prop="Reagent">
                <el-radio-group v-model="formdoc.Reagent">
                    <el-radio :label="0">GlobalFiler</el-radio>
                    <el-radio :label="1">PowerPlex®21</el-radio>
                    <el-radio :label="2">Identifiler Plus</el-radio>
                </el-radio-group>
            </el-form-item>
            <el-form-item label="第一鉴定人" prop="Firster">
                <el-radio-group v-model="formdoc.Firster">
                    <el-radio :label="0">LXY</el-radio>
                    <el-radio :label="1">LT</el-radio>
                </el-radio-group>
            </el-form-item>
            <el-form-item label=" " style="margin-left:0px;">
                <el-button type="primary" @click="onIdentity">生成鉴定书</el-button>
                <el-button type="primary" @click="onReport">生成检验报告</el-button>
            </el-form-item>
        </el-form>
        <!-- 查询区----end -->
        <!-- 操作区----start -->
    </div>
</template>

<style lang="scss">
// 设置输入框的宽度
._makedoc{
    padding-left:180px;
    padding-top:100px;

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
}
</style>

<script>
import apis from '../../apis/apis';
export default {
    name: 'makedoc',
    data() {
        return {
            formdoc: {
                Controlurl:'',
                Sampleids:'',
                Reagent:0,
                Firster:0,
            },
            rulesEdit: {
                Controlurl: [
                    { required: true, message: "请输入确认书网址", trigger: "blur" },
                ],
            },
            labelPosition: 'right', //lable对齐方式
            labelWidth: '100px', //lable宽度
        };
    },
    computed:{     
    },
    filters: {
        
    },
    mounted(){
        this.onIdentity();
        this.onReport();
        this.initCKEditor()
    },
    methods: {
        // onReset(){
        //     this.$refs['formdoc'].resetFields();
        // },
    }
};
</script>
