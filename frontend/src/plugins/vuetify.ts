import { createVuetify } from 'vuetify';
import { aliases, mdi } from 'vuetify/iconsets/mdi-svg';
import 'vuetify/styles';

export default createVuetify({
  theme: {
    defaultTheme: 'dark',
    themes: {
      light: {
        colors: {
          primary: '#1867C0',
          secondary: '#5CBBF6',
          alert: '#DF0000',
          monochrome: '#404040',
          basetext: '#202020',
          background00: '#D8D8D8',
          background01: '#E8E8E8',
          background02: '#F8F8F8',
        },
      },
      dark: {
        colors: {
          primary: '#58A7FF',
          secondary: '#1C7BB6',
          alert: '#DF0F0F',
          monochrome: '#BFBFBF',
          basetext: '#DFDFDF',
          background00: '#333333',
          background01: '#0F0F0F',
          background02: '#111111',
        },
      },
    },
  },
  icons: {
    defaultSet: 'mdi',
    aliases,
    sets: {
      mdi,
    },
  },
});
