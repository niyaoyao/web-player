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
    .music-play-next-button(@click="playPrevious")
      .music-play-next-icon-filter.music-play-previous-icon
    .music-progress-bar
    .music-play-next-button(@click="playNext")
      .music-play-next-icon-filter.music-play-next-icon
    .music-play-mode-button(@click="changePlayMode")
      .music-play-mode-icon.music-play-mode-repeat-icon
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

function requestPlayList() {
  let url = "musics/musics.json"
  axios.get(url).then((response) => {
     musicNames.value = response.data.map((file:string) => file.substring(0, file.lastIndexOf(".")));
    musicUri.value = response.data.map((m:string) => '/musics/' + m)
  })
}
requestPlayList()

var currentIndex = ref(0);
enum PlayMode {
  Loop = "🔁",
  Single = "🔂",
  Random = "🔀"
}

var playMode:Ref<PlayMode> = ref(PlayMode.Loop)
function changePlayMode() {
  let playModeButton = document.querySelector(".music-play-mode-icon")!;
  var playModeIcon = "music-play-mode-icon music-play-mode-repeat-icon"
  switch (playMode.value) {
    case PlayMode.Loop:
      playMode.value = PlayMode.Single
      playModeIcon = "music-play-mode-icon music-play-mode-repeat-1-icon"
      break;
    case PlayMode.Single:
      playMode.value = PlayMode.Random
      playModeIcon = "music-play-mode-icon music-play-mode-shuffle-icon"
      break;
    case PlayMode.Random:
      playMode.value = PlayMode.Loop
      playModeIcon = "music-play-mode-icon music-play-mode-repeat-icon"
      break;
    default:
      playMode.value = PlayMode.Loop
      playModeIcon = "music-play-mode-icon music-play-mode-repeat-icon"
      break;
  }
  playModeButton.setAttribute("class", playModeIcon);

  console.log(playMode.value);
  
}

function itemStyle(index: number) {
  let isPlaying = currentIndex.value == index;
  return isPlaying ? 'color:#8d91aa;background-color:#f3f1ef' : '';
}
function musicItemDidClick(index: number) {
  currentIndex.value = index;
  playLoopMusic()
}

function playNext() {
  currentIndex.value = currentIndex.value + 1;
  currentIndex.value = currentIndex.value % musicUri.value.length;
  playLoopMusic();
}

function playPrevious() {
  currentIndex.value = currentIndex.value - 1 >= 0 ? currentIndex.value - 1 : musicNames.value.length - 1;
  currentIndex.value = currentIndex.value % musicUri.value.length;
  playLoopMusic();
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
    switch (playMode.value) {
      case PlayMode.Loop:
        currentIndex.value = currentIndex.value + 1
        break;
      case PlayMode.Single:
        currentIndex.value = currentIndex.value
        break;
      case PlayMode.Random:
        currentIndex.value = Math.floor(Math.random() * musicUri.value.length)
        break;
      default:
        currentIndex.value = currentIndex.value + 1
        break;
    }
    
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
    height 600px
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
    align-items center
    .music-progress-bar
      flex: 1
    .music-play-next-button
      width 54px
      display flex
      justify-content center
      align-items center
      cursor pointer
      .music-play-previous-icon
        background-image url(/icons/skip-start-fill.svg)
      .music-play-next-icon
        background-image url(/icons/skip-end-fill.svg)
      .music-play-next-icon-filter
        background-size 30px 30px
        width 30px
        height 30px
        filter invert(63%) sepia(16%) saturate(378%) hue-rotate(194deg) brightness(89%) contrast(90%)
    .music-play-mode-button
      width 54px
      display flex
      justify-content center
      align-items center
      cursor pointer
      .music-play-mode-repeat-icon
        background-image url(/icons/repeat.svg)
      .music-play-mode-repeat-1-icon
        background-image url(/icons/repeat-1.svg)
      .music-play-mode-shuffle-icon
        background-image url(/icons/shuffle.svg)
      .music-play-mode-icon
        background-size 30px 30px
        width 30px
        height 30px
        filter invert(63%) sepia(16%) saturate(378%) hue-rotate(194deg) brightness(89%) contrast(90%)
    .music-play-button
      width 35px
      height 35px
      display flex
      justify-content center
      align-items center
      border-radius 60px
      border 2px solid #8d91aa
      cursor pointer
      .music-button-icon
        background-size 30px 30px
        width 30px
        height 30px
        filter invert(63%) sepia(16%) saturate(378%) hue-rotate(194deg) brightness(89%) contrast(90%)
      .music-play-icon
        background-image url(/icons/play-fill.svg)
      .music-pause-icon
        background-image url(/icons/pause-fill.svg)

</style>
