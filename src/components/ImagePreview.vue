<template>
  <div class="image-preview" v-if="selectedItem">
    <v-card>
      <v-card-title>{{ selectedItem.name }}</v-card-title>
      <v-img :src="selectedItem.image" class="bg-grey-lighten-2" :max-height="500" cover></v-img>
      <v-card-text> Number of Clicks: {{ selectedItem.clicks }} </v-card-text>
    </v-card>
  </div>
  <div v-else class="image-preview">
    <v-card>
      <v-card-text> Select an item to see the image </v-card-text>
    </v-card>
  </div>
</template>

<script>
export default {
  props: {
    selectedItem: {
      type: Object,
      default: null
    }
  }
}
</script>
