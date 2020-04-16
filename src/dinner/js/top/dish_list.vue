<template>
    <div class="com-top-dish">
        <div class="row" v-for="row in ctx.rows" :key="row.pk">
            <div class="myimage" :style="get_style(row)"></div>
            <div class="content">
                <span v-text="row.label"></span>
                <span v-text="row.title"></span>
                <div class="price-pannel" style="display: flex">
                    <div class="price">￥ <span v-text="row.price"></span></div>
                    <div>
                        <van-stepper v-model="row.count" :default-value="0" min="0" max="300"  @change="on_change(row)"/>
                    </div>

                </div>


            </div>
        </div>
    </div>
</template>
<script>
    export default {
        props:['ctx'],
        data(){
            var parStore = ex.vueParStore(this)
            var last_ps = live_root.lastsibe(parStore.vc).childStore
            return {
                last_ps:last_ps,
                parStore:parStore
            }
        },
        mounted(){
//            this.parStore.$on('finish-search',this.adapt_rows)
            this.parStore.filter_load_row = this.adapt_rows
        },
        methods:{
            adapt_rows(new_rows){
                for(var i=0;i<new_rows.length;i++){
                    var row = new_rows[i]
                    var selectd = ex.findone(this.last_ps.rows,{pk:row.pk})
                    if(selectd){
                        new_rows.splice(i,1,selectd)
                    }else{
                        debugger
                        this.last_ps.rows.push(row)
                    }
                }
                return new_rows
            },
            get_style(row){
                return {'background-image':'url('+row.cover+')'}
            },
            on_change(row){
                this.last_ps.$emit('dish-count-change',row)
            }
        }
    }
</script>
<style scoped lang="scss">
    .com-top-dish{
        background-color: white;
        height: calc( var( --app-height ) - 1rem );
        overflow-y: auto;
    }

    .row{
        padding: .2rem;
        display: flex;
    }
    .myimage{
        background-size: cover;
        background-position: center;
        width: 1.6rem ;
        height: 1.6rem;
    }
    .content{
        padding: .3rem 0 .2rem .2rem;
        flex-grow: 100;
    }
    .price{
        color: red;
        font-size: .3rem;
    }
    .price-pannel{
        display: flex;
        justify-content: space-between;
        margin: .4rem 0 .2rem 0
    }
</style>