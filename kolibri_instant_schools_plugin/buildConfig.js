module.exports = [
  {
    bundle_id: 'instant_schools_auth',
    webpack_config: {
      entry: './assets/src/authApp.js'
    },
  },
  {
    bundle_id: 'instant_schools_about',
    webpack_config: {
      entry: './assets/src/aboutApp.js'
    },
  },
  {
    bundle_id: 'instant_schools_about_nav_action',
    webpack_config: {
      entry: './assets/src/views/SideNav/AboutSideNavEntry.js',
    },
  },
  {
    bundle_id: 'instant_schools_login_nav_action',
    webpack_config: {
      entry: './assets/src/views/SideNav/LoginSideNavEntry.js',
    },
  },
];
