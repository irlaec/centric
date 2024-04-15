import { createApp } from 'vue'
import App from './App.vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'

import ImagePreview from '@/components/ImagePreview.vue'
import ImageList from '@/components/ImageList.vue'
import ImageListItem from '@/components/ImageListItem.vue'

const app = createApp(App)
const vuetify = createVuetify({
  components,
  directives
})
app.component('image-preview', ImagePreview)
app.component('image-list', ImageList)
app.component('image-list-item', ImageListItem)
app.use(vuetify).mount('#app')
