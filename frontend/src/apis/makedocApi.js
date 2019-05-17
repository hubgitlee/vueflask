import Axios from "axios";

/**
 * 提供kbms相关接口
 */
export default {
    add:function({SampleID,D3S1358,vWA,D16S539,CSF1PO,TPOX,Yindel,Amel,D8S1179,D21S11,D18S51,DYS391,D2S441,D19S433,TH01,FGA,D22S1045,D5S818,D13S317,D7S820,SE33,D10S1248,D1S1656,D12S391,D2S1338}){
         var param={
                SampleID:SampleID,//标题
                D3S1358:D3S1358,
                vWA:vWA,
                D16S539:D16S539,
                CSF1PO:CSF1PO,
                TPOX:TPOX,
                Yindel:Yindel,
                Amel:Amel,
                D8S1179:D8S1179,
                D21S11:D21S11,
                D18S51:D18S51,
                DYS391:DYS391,
                D2S441:D2S441,
                D19S433:D19S433,
                TH01:TH01,
                FGA:FGA,
                D22S1045:D22S1045,
                D5S818:D5S818,
                D13S317:D13S317,
                D7S820:D7S820,
                SE33:SE33,
                D10S1248:D10S1248,
                D1S1656:D1S1656,
                D12S391:D12S391,
                D2S1338:D2S1338,
        };
        console.log(param);
        return Axios.post('/add', param);
    },
    update:function({id,title,content,keywords,depositoryBank,businessType,businessScene,publicState}){
        var param={
            id:id,
            title: title,
            content:content,//内容
            keywords:keywords,
            depositoryBank:depositoryBank,//存管银行
            businessType:businessType,//业务类型
            businessScene:businessScene,//业务场景
            publicState:publicState,//发布状态
       };
       return Axios.post('/api/kbms-api/update', param);
   },
   delete:function({id}){
        var param={
            id:id
        };
        return Axios.post('/delete', param);
    },
    deleteBatch:function({ids}){
        var param={
            ids:ids
        };
        return Axios.post('/api/kbms-api/deleteBatch', param);
    },
    updatePublicState:function({id,publicState}){
        var param={
            id:id,
            publicState:publicState
        };
        return Axios.post('/api/kbms-api/updatePublicState', param);
    },
    getList({SampleID,
        D3S1358,
        vWA,
        D16S539,
        CSF1PO,
        TPOX,
        Yindel,
        Amel,
        D8S1179,
        D21S11,
        D18S51,
        DYS391,
        D2S441,
        D19S433,
        TH01,
        FGA,
        D22S1045,
        D5S818,
        D13S317,
        D7S820,
        SE33,
        D10S1248,
        D1S1656,
        D12S391,
        D2S1338,
        add_time,
        currentPage,
        pageSize }){
        var param={
                SampleID:SampleID,//标题
                D3S1358:D3S1358,
                vWA:vWA,
                D16S539:D16S539,
                CSF1PO:CSF1PO,
                TPOX:TPOX,
                Yindel:Yindel,
                Amel:Amel,
                D8S1179:D8S1179,
                D21S11:D21S11,
                D18S51:D18S51,
                DYS391:DYS391,
                D2S441:D2S441,
                D19S433:D19S433,
                TH01:TH01,
                FGA:FGA,
                D22S1045:D22S1045,
                D5S818:D5S818,
                D13S317:D13S317,
                D7S820:D7S820,
                SE33:SE33,
                D10S1248:D10S1248,
                D1S1656:D1S1656,
                D12S391:D12S391,
                D2S1338:D2S1338,
                add_time:add_time,//添加时间
            currentPage:currentPage,
            pageSize:pageSize
        };
        // return Axios.post('/api/kbms-api/queryList', param);
        return Axios.post('/queryList', param);
    },
    getOne({id}){
        var param={
            id:id
        };
        return Axios.post('/api/kbms-api/getOne', param);
    }
}