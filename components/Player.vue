<template lang="pug">

.player-panel
  .music-list
    .music-item(
      v-for="(music, index) in musicList"
      :item="music"
      :style="itemStyle(index)"
      @click="musicItemDidClick(index)"
      ) {{musicList[index]}}
  .music-player
    .music-play-icon
  audio(controls ref='audio')
    source(src='/musics/离别开出花.mp4')
</template>

<script setup lang="ts">
useHead(() => ({
  title: 'NY Player',
  meta: [
    { name: 'description', content: 'This is NY Player page description' },
  ],
  link: [
    { rel: 'icon', href: "data:;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAWJAAAFiQFtaJ36AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJgSURBVHgBpZTLaxNRFMa/mUmapklj05BEgo8i+EAwFquiVly4MT7A/0BQdONOunPtuiCCXShCqVtFAurOUEEUu7BoXUiTUAspZkwmSZNhapN0/O4kSkgzSasHfnNP7j3z5ZyTmwM0zE/ukR/E3CYpMkmGmlqIkOQ/CLXzjeyQ+Jgm12BjZ66GoHB1tKA0mZ3VUCzWWsOnhOAacdkJTs6fxsEjXnjpe5nHIKSGz/X29QU8ncm0huflbmLCPrzJ4ycrUulnJYGJrPC5Fx0fag8PyOhhnxOaJaZaog1hVYiS0cuBTfGOXoKpRAErRh0+twwPy/zyvoD4xCJEJkqH+J6C1Uodi3MljJzzw2CGyoEBJD+WYJqd4+1LZr/CNyM48fYYcNQLjSXmuW0EnAiODtq+1jFDySFhdzyK4diw9Y0VqovL4aboL66h836on8rYcoahh2fRHzvEEt0oU6zIUgtE41mO+C4GYGcdBavpGirPK6hrAWYWYFYuZgmsUlSIy6d8kAc6d0tcbKu9ktcNz6Xj8Fw4DM+V/VCCJg+FTMmSEsjMV8E6+vhJf5mH/ioPjauxvLZZ8I8594UxkpwSr5CyhWStFK2VYLxLQ3+dQeHBEkxjwz7DVts19wj9Y3t5KEQrf2kIl7C+8B1L0RfYcg+1u48hppHJ/pkI0g+RMP2dJAL1zjzsTFz2CbT9n6vpDKqpFbhOjkHxiVHpJH0wV+vI3piGHv9qp6d2HV+y3wdPbBzKnjDquRz0ZwlsFHV0sSfiIVIQw/F/B6zog0eULH7zmeamaJgYd7VtsEzuk1tE/w3RrgBC1TLQegAAAABJRU5ErkJggg==" },
  ],
}));

let musicList = [
  "大风吹",
  "婚姻常识",
  "漠河舞厅",
  "勇气大爆发",
  "圣斗士星矢",
  "离别开出花",
  "Believer",
  "Digital_monster",
  "SlamDunk",
  "please_dont_go",
]
let musicUri = musicList.map((m) => '/musics/' + m + '.mp4');
console.log(musicUri);
var playingIndex = 0;
function itemStyle(index: number) {
  let isPlaying = playingIndex == index;
  return isPlaying ? 'color:#88AB8E;background-color:#F2F1EB' : '';
}
function musicItemDidClick(index: number) {
  playingIndex = index;
  console.log(index);
  this.$set(this.musicList, index);
}
</script>

<style lang="stylus" scoped>
.player-panel
  color #666666
  margin 0 auto
  padding 0 auto
  .music-list
    overflow scroll
    height 200px
    background-color #eadfbc
    .music-item
      display block
      font-size 20px
      line-height 40px
      text-align center
      font-family sans-serif
    .music-item:hover
      background-color #EEE7DA
  .music-player
    background-color #AFC8AD
    height 60px
    padding 0
    .music-play-icon
      mask-image url(/icons/play.svg)
      width 60px
      height 60px
  .icon-play
    mask-image: url(icon.svg);
  .iconfont 
    font-family "iconfont" !important
    font-size 16px
    font-style normal
    -webkit-font-smoothing antialiased
    -moz-osx-font-smoothing grayscale
  
  .icon-play_solid:before 
    content "\e6de"
  

  .icon-stop_solid:before 
    content "\e67a"
  

  .icon-iconfont_loading_outline:before 
    content "\e6a7"
  

</style>