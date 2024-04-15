<template>
  <div class="image-list-item" @click="handleItemClick">
    <div class="item-name">{{ item.name }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      clicks: 0
    }
  },
  props: {
    item: {
      type: Object,
      required: true
    }
  },
  methods: {
    handleItemClick() {
      this.clicks++
      this.$emit('item-clicked', { ...this.item, clicks: this.clicks })
    }
  }
}
</script>

<style scoped>
.image-list-item {
  cursor: pointer;
  padding: 10px;
  margin-bottom: 10px;
  background-color: #f2f2f2;
  border-radius: 5px;
}

.image-list-item:hover {
  background-color: #e6e6e6;
}

.item-image {
  width: 100px;
  height: 100px;
  margin-bottom: 5px;
}

.item-name {
  text-align: center;
}
</style>
