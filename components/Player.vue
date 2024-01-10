<template lang="pug">

.player-panel
  .music-list
    .music-item(
      v-for="(music, index) in musicNames"
      :item="music"
      :style="itemStyle(index)"
      :id="'list-item-' + (index)"
      @click="musicItemDidClick(index)"
      ) {{musicNames[index]}}
  .music-player
    .music-play-button(@click="playMusic(false)")
      .music-button-icon.music-play-icon
  audio(style="display:none" ref="audioplayer" @timeupdate="updateAudioTime")

</template>

<script setup lang="ts">
import axios from 'axios';

useHead(() => ({
  title: 'NY Player',
  meta: [
    { name: 'description', content: 'This is NY Player page description' },
  ],
  link: [
    { rel: 'icon', href: "data:;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAAWJAAAFiQFtaJ36AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAJgSURBVHgBpZTLaxNRFMa/mUmapklj05BEgo8i+EAwFquiVly4MT7A/0BQdONOunPtuiCCXShCqVtFAurOUEEUu7BoXUiTUAspZkwmSZNhapN0/O4kSkgzSasHfnNP7j3z5ZyTmwM0zE/ukR/E3CYpMkmGmlqIkOQ/CLXzjeyQ+Jgm12BjZ66GoHB1tKA0mZ3VUCzWWsOnhOAacdkJTs6fxsEjXnjpe5nHIKSGz/X29QU8ncm0huflbmLCPrzJ4ycrUulnJYGJrPC5Fx0fag8PyOhhnxOaJaZaog1hVYiS0cuBTfGOXoKpRAErRh0+twwPy/zyvoD4xCJEJkqH+J6C1Uodi3MljJzzw2CGyoEBJD+WYJqd4+1LZr/CNyM48fYYcNQLjSXmuW0EnAiODtq+1jFDySFhdzyK4diw9Y0VqovL4aboL66h836on8rYcoahh2fRHzvEEt0oU6zIUgtE41mO+C4GYGcdBavpGirPK6hrAWYWYFYuZgmsUlSIy6d8kAc6d0tcbKu9ktcNz6Xj8Fw4DM+V/VCCJg+FTMmSEsjMV8E6+vhJf5mH/ioPjauxvLZZ8I8594UxkpwSr5CyhWStFK2VYLxLQ3+dQeHBEkxjwz7DVts19wj9Y3t5KEQrf2kIl7C+8B1L0RfYcg+1u48hppHJ/pkI0g+RMP2dJAL1zjzsTFz2CbT9n6vpDKqpFbhOjkHxiVHpJH0wV+vI3piGHv9qp6d2HV+y3wdPbBzKnjDquRz0ZwlsFHV0sSfiIVIQw/F/B6zog0eULH7zmeamaJgYd7VtsEzuk1tE/w3RrgBC1TLQegAAAABJRU5ErkJggg==" },
  ],
}));
var isPlaying = false;
var musicUri = ref([])
var musicNames = ref([])
let url = "https://github.com/niyaoyao/web-player/blob/main/public/musics/musics.json" // "musics/musics.json"
axios.get(url).then((response) => {
  musicNames.value = response.data
  musicUri.value = response.data.map((m:string) => '/musics/' + m + '.mp4')
})

var currentIndex = ref(0);

function itemStyle(index: number) {
  let isPlaying = currentIndex.value == index;
  return isPlaying ? 'color:#8d91aa;background-color:#f3f1ef' : '';
}
function musicItemDidClick(index: number) {
  currentIndex.value = index;
  playLoopMusic()
}

function playLoopMusic() {
  playMusic(true);
}

function play(audio:HTMLAudioElement, playerButton: Element, index: Number) {
  audio.play();
  isPlaying = true;
  playerButton.setAttribute("class", "music-button-icon music-pause-icon");
  document.getElementById("list-item-" + index)!.scrollIntoView()
}

function pause(audio:HTMLAudioElement, playerButton: Element) {
  audio.pause();
  isPlaying = false;
  playerButton.setAttribute("class", "music-button-icon music-play-icon");
}

function playMusic(shouldLoop: boolean) {
  let audio:HTMLAudioElement = document.querySelector("audio")!;
  let playerButton = document.querySelector(".music-button-icon")!;
  audio.setAttribute("src",musicUri.value[currentIndex.value]);
  if (isPlaying) {
    if (shouldLoop) {
      console.log("Loop Play: " + currentIndex.value);
      play(audio, playerButton, currentIndex.value)
    } else {
      console.log("Pause");
      pause(audio, playerButton)
    }
  } else {
    if (isPlaying) {
      console.log("Pause");
      pause(audio, playerButton)
    } else {
      console.log("Play: " + currentIndex.value);
      play(audio, playerButton, currentIndex.value)
    }
  }

}

function updateAudioTime() {
  let audio: HTMLAudioElement = document.querySelector("audio")!;
  const percentagePosition = (audio.currentTime) / audio.duration;
  if (percentagePosition >= 0.99999999) {
    currentIndex.value = currentIndex.value + 1
    currentIndex.value = currentIndex.value % musicUri.value.length
    console.log(currentIndex.value);
    playLoopMusic();
  }

}
</script>

<style lang="stylus" scoped>
.player-panel
  color #666666
  margin 0 auto
  padding 0 auto
  .music-list
    overflow scroll
    height 300px
    background-color #fff
    .music-item
      display block
      font-size 20px
      line-height 40px
      text-align center
      font-family sans-serif
      border-radius 10px
      cursor pointer
    .music-item:hover
      background-color #f9f5f2
      border-radius 10px
  .music-player
    background-color #dce2ec
    height 60px
    padding 0
    display flex
    flex-direction row
    justify-content flex-start
    padding 10px 15px
    border-radius 10px
    .music-play-button
      width 54px
      height 54px
      display flex
      justify-content center
      align-items center
      border-radius 60px
      border 3px solid #8d91aa
      cursor pointer
      .music-button-icon
        background-size 30px 30px
        width 30px
        height 30px
        filter invert(63%) sepia(16%) saturate(378%) hue-rotate(194deg) brightness(89%) contrast(90%)
      .music-play-icon
        background-image url(/icons/play.png)
      .music-pause-icon
        background-image url(/icons/pause.png)

</style>
