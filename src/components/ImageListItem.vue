<template>
  <div class="image-list-item" @click="handleItemClick">
    <v-col>
      <v-btn size="x-large" block>{{ item.name }}</v-btn>
    </v-col>
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
