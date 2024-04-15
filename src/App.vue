<template>
  <div id="app">
    <v-container>
      <v-row no-gutters>
        <v-col cols="2">
          <v-sheet class="pa-2 ma-2">
            <image-list :items="items" @item-selected="handleItemSelected"></image-list>
          </v-sheet>
        </v-col>
        <v-col>
          <v-sheet class="pa-2 ma-2">
            <image-preview :selected-item="selectedItem"></image-preview>
          </v-sheet>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
const CAT_API_URL = 'https://api.thecatapi.com/v1/images/search?limit=10'
export default {
  name: 'App',
  data() {
    return {
      items: [],
      selectedItem: null
    }
  },
  mounted() {
    this.fetchCatImages()
  },
  methods: {
    async fetchCatImages() {
      try {
        const response = await fetch(CAT_API_URL)
        const data = await response.json()
        this.items = data.map((item, index) => ({
          id: item.id,
          name: `Cat ${index + 1}`,
          image: item.url
        }))
      } catch (error) {
        console.error('Error fetching data:', error)
      }
    },
    handleItemSelected(item) {
      this.selectedItem = item
    }
  }
}
</script>
