<template>
    <div class="com-live-comfirm-dish-list">
        <com-uis-nav-bar :title="ctx.title" :back_action="ctx.back_action"></com-uis-nav-bar>
        <div class="content">
            <div class="item" v-for="row in ctx.rows">
                <div class="dish-name" v-text="row.label"></div>
                <div>
                    <span v-text="row.count"></span>
                    <span>份</span>
                </div>

            </div>
            <div style="width: 90vw;margin: .4rem auto">
                <van-button size="large" type="primary" @click="on_click()">给爷上菜</van-button>
            </div>

        </div>

    </div>
</template>
<script>
export default {
    props:['ctx'],
    basename:'live-comfirm-dish-list',
    methods:{
        on_click(){
            cfg.toast('正在杀猪宰羊中，请您稍等!')

//            setTimeout(()=>{
//                ex.each(this.ctx.rows,(row)=>{
//                    row.count= 0
//                 })
//            },2000)

            //                live_root.lastsibe(this).selected_row=[]

        }
    }
}
</script>
<style scoped lang="scss">
.com-live-comfirm-dish-list{
    height: 100%;
    background-color: white;
}
    .item{
        height: .8rem;
        line-height: .8rem;
        display: flex;
    }
    .dish-name{
        width: 5rem;
        padding-left: .3rem;
    }
</style>