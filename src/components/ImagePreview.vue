<!-- ItemDetail.vue -->
<template>
  <div class="image-preview" v-if="selectedItem">
    <h2>{{ selectedItem.name }}</h2>
    <img :src="selectedItem.image" alt="Item Image" class="item-image" />
    <p>Number of Clicks: {{ selectedItem.clicks }}</p>
  </div>
  <div v-else>
    <p>Select an item to see details.</p>
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

<style scoped>
.image-preview {
  padding: 20px;
}

.item-image {
  width: 200px;
  height: 200px;
  cursor: pointer;
}
</style>
