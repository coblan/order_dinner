<template>
    <div class="com-top-dish-submit">
        <div class="confirm-pannel" >
            <div class="list">
                <div class="item dish-item" v-for="row in parStore.selected_row" :key="row.pk">
                    <div class="dish-name" v-text="row.label"></div>
                    <div>
                        <van-stepper v-model="row.count" :default-value="0" min="0" max="300"  />
                    </div>
                </div>
            </div>

            <div class="close-btn">
                <van-icon name="close" size=".4rem" @click="on_close" />
            </div>

        </div>

        <div class="content" style="display: flex" @click="on_content_click">
            <div class="cart">
                <img src="/static/images/chart_car.png" alt="">
                <div class="my-number" v-text="dish_count"></div>
            </div>
            <div class="total-text">
                共 <span v-text="total_amount"></span> 元
            </div>
        </div>

        <div class="submit-btn" style="z-index:2" @click="on_submit()">给爷上菜</div>

    </div>
</template>
<script>
    export default {
        props:['ctx'],
        data(){
            var parstore = ex.vueParStore(this)
            parstore.dish = {}
            parstore.selected_row =[]
            return {
                parStore:parstore,
                dish_count:0,
                total_amount:0,

            }
        },
        mounted(){
            this.parStore.$on('dish-count-change',this.update_info)
//            var ele = $(this.$el).find('.confirm-pannel')
//            ex.append_css(`.confirm-pannel{bottom:${-ele.height}`)

            var element = $(this.$el).find('.confirm-pannel')
            this.old_bottom = element.css('bottom')
            this.old_top = element.css('top')
        },
        methods:{
            on_close(){
//                $(this.$el).find('.confirm-pannel').velocity({
//                    top:'0rem',
//                    bottom:this.old_bottom,
//                },500)
                $.Velocity.animate( $(this.$el).find('.confirm-pannel'), {
                    top:'0rem',
                    bottom:this.old_bottom,
                },500).then((element)=>{
                    $(element).removeAttr("style")
            })

//                $(this.$el).find('.confirm-pannel').removeClass('opened')
            },
            on_content_click(){
                console.log('jj')
//                var element =  $(this.$el).find('.confirm-pannel')
//                element.css('bottom',-element.height)
//                $(this.$el).find('.confirm-pannel').addClass('opened')

                var element = $(this.$el).find('.confirm-pannel')
                element.velocity({
//                    top:this.old_top,
                    bottom:'1rem'
                },500)

            },
            update_info(row){
                if(row.count >0){
                    if( ! ex.isin(row,this.parStore.selected_row)){
                        this.parStore.selected_row.push(row)
                    }
                }else{
                    if( ex.isin(row,this.parStore.selected_row)){
                        ex.remove(this.parStore.selected_row,row)
                    }
                }
                console.log('row length = ' +this.parStore.selected_row.length)

                var count = 0
                var total_amount = 0
                ex.each(this.parStore.selected_row,row=>{
                    count += row.count
                    total_amount += (row.price* row.count)
                })

//                for(var k in this.parStore.dish){
//                    count += this.parStore.dish[k].count
//                }
                this.dish_count= count
                this.total_amount= total_amount.toFixed(2)
            },
            on_submit(){
                cfg.toast("请您稍等!")
//                ex.each(this.selected_row,(row)=>{
//                    row.count=0
//                })
//                this.selected_row = []
//                live_root.open_live('live_comfirm_dish_list',{title:'菜单确认',rows:this.selected_row})
            }
        },
        computed:{

        }
    }
</script>
<style lang="scss" scoped>
.com-top-dish-submit{
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    display: flex;
    align-items: stretch;
    justify-content: space-between;
    height: 1rem;
    /*width: var( --app-width );*/
}
.content{
    display: flex;
    line-height: 1rem;
    padding-left: .2rem;
    background-color: grey;
    flex-grow: 10;
    z-index: 2;
}

.cart{
    position: relative;
    img{
        width: .6rem;
        height: .6rem;
        vertical-align: middle;
    }
    .my-number{
        width: .4rem;
        height:.4rem;
        background-color: #f68a19;
        color: white;
        position: absolute;
        top: 0rem;
        right: -.2rem;
        line-height: .4rem;
        text-align: center;
        border-radius: .2rem;
    }
}
.total-text{
    margin-left: .3rem;
    color: white;
}
    .submit-btn{
        background-color: #f68a19;
        color: white;
        line-height: 1rem;
        width: 2rem;
        text-align: center;
    }
    .confirm-pannel{
        position: absolute;
        background-color: white;
        padding-top: .6rem;
        background-color: #fafafa;
        border-top-right-radius: .3rem;
        border-top-left-radius: .3rem;
        border-top:1px solid #b9b9b9;
        /*z-index: -1;*/
        width: 100%;

        .list{
            max-height: 50vh;
            overflow-y: auto;
        }

        .close-btn{
            position: absolute;
            right: .1rem;
            top:.1rem;
        }

        .dish-item{
            padding: .2rem 0.2rem .2rem .3rem;
            display:flex;
            justify-content: space-between;
        }
    }

</style>