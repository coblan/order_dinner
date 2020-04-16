<template>
    <div class="com-dish-header">
        <div class="my-wrap">
            <div>
                <img src="/static/images/eat.png" alt="">
                5号桌
            </div>

        </div>
        <div class="my-wrap">
            <div>
                <van-icon name="search"  @click="go_search" size=".4rem" />
            </div>

        </div>
    </div>
</template>
<script>
    export default {
        prop:['ctx'],
        methods:{
            go_search(){
                live_root.open_live('live_search_list',{director_name:'dish.user',table_editor:'com-top-dish-list'})
            }
        }
    }
</script>
<style scoped lang="scss">
.com-dish-header{
    display: flex;
    justify-content: space-between;
    height: 1rem;
    line-height: 1rem;
    background-color: #f86351;
    color: white;
    .my-wrap{
        padding: 0 .3rem;
        img{
            height: .6rem;
            width: auto;
            vertical-align: middle;
        }
        .van-icon{
            vertical-align: middle;
        }
}
}
</style>
