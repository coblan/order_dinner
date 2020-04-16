<template>
    <div class="com-dinner-list">
        <div class="row" :key="row.pk" v-for="row in rows">
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
            var parstore = ex.vueParStore(this)
            parstore.rows =   parstore.rows || []
            return {
                rows:[],
                parStore:parstore
            }
        },
        mounted(){
            ex.director_call('dish.user',{kind:this.ctx.kind}).then(resp=>{
                for (var i=0;i<resp.rows.length;i++) {
                    var row = resp.rows[i]
                    var find_row = ex.findone(this.parStore.rows ,{pk:row.pk})
                    if(find_row){
                        resp.rows.splice(i,1,find_row)
                    }else{
                        this.parStore.rows.push(row)
                    }
                }
                this.rows = resp.rows

            })
        },
        methods:{
            get_style(row){
              return {'background-image':'url('+row.cover+')'}
            },
            on_change(row){
                console.log(row.count)
//                Vue.set(this.parStore.dish,row.pk,row)
                this.parStore.$emit('dish-count-change',row)
//                this.parStore.dish[row.pk] = row
            }
        }

    }
</script>

<style lang="scss" scoped>

.com-dinner-list{

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
    /*img{*/
        /*width: 2rem;*/
    /*}*/
}
</style>