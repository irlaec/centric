<!-- App.vue -->
<template>
  <div id="app">
    <image-list :items="items" @item-selected="handleItemSelected"></image-list>
    <image-preview :selected-item="selectedItem"></image-preview>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      items: [
        { id: 1, name: 'Item 1', image: 'item1.jpg' },
        { id: 2, name: 'Item 2', image: 'item2.jpg' },
        { id: 3, name: 'Item 3', image: 'item3.jpg' }
      ],
      selectedItem: null
    }
  },
  methods: {
    handleItemSelected(item) {
      console.log('Selected item:', item)
      this.selectedItem = item
      console.log('Selected item:', item)
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
