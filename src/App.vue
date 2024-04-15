<template>
  <div id="app">
    <image-list :items="items" @item-selected="handleItemSelected"></image-list>
    <image-preview :selected-item="selectedItem"></image-preview>
  </div>
</template>

<script>
const CAT_API_URL = 'https://api.thecatapi.com/v1/images/search?limit=10';
export default {
  name: 'App',
  data() {
    return {
      items: [],
      selectedItem: null
    }
  },
  mounted() {
    this.fetchCatImages();
  },
  methods: {
    async fetchCatImages() {
      try {
        const response = await fetch(CAT_API_URL);
        const data = await response.json();
        this.items = data.map((item, index) => ({
          id: item.id,
          name: `Cat ${index + 1}`,
          image: item.url
        }));
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    handleItemSelected(item) {
      this.selectedItem = item
    }
  }
}
</script>

<style>
#app {
  display: flex;
  justify-content: space-between;
}
</style>
