<template>
  <div>
    <div v-for="(item, index) in items" :key="index">
      <image-list-item :item="item" @item-clicked="handleItemClick"></image-list-item>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    items: {
      type: Array,
      required: true
    }
  },
  methods: {
    handleItemClick(item) {
      this.$emit('item-selected', item)
    }
  }
}
</script>
