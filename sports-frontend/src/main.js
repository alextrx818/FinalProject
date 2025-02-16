import { createApp } from 'vue'
import { 
  Quasar,
  QLayout,
  QHeader,
  QToolbar,
  QToolbarTitle,
  QPage,
  QPageContainer,
  QTable,
  QTd,
  QCard,
  QCardSection,
  QChip,
  QIcon,
  QSpace,
  QSpinner
} from 'quasar'

// Import icon libraries
import '@quasar/extras/material-icons/material-icons.css'

// Import Quasar css
import 'quasar/dist/quasar.css'

import App from './App.vue'

const app = createApp(App)

app.use(Quasar, {
  components: {
    QLayout,
    QHeader,
    QToolbar,
    QToolbarTitle,
    QPage,
    QPageContainer,
    QTable,
    QTd,
    QCard,
    QCardSection,
    QChip,
    QIcon,
    QSpace,
    QSpinner
  }
})

app.mount('#app')
