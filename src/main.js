import { createApp } from 'vue'
import App from './App.vue'
import ImagePreview from '@/components/ImagePreview.vue'
import ImageList from '@/components/ImageList.vue'
import ImageListItem from '@/components/ImageListItem.vue'

const app = createApp(App)
app.component('image-preview', ImagePreview)
app.component('image-list', ImageList)
app.component('image-list-item', ImageListItem)
app.mount('#app')
