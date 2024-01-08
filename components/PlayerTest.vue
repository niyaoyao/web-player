<template>
    <div>Player</div>
    <button  @click="show = !show">Test</button>
    <div> {{ show }} </div>
</template>

<script setup lang="ts">
const show = ref(false)

</script>