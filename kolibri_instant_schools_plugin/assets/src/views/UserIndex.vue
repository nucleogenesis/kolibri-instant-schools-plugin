<template>

  <component
    :is="pageName === PageNames.SIGN_IN ? 'div' : 'ImmersivePage'"
    :route="{ name: PageNames.SIGN_IN }"
  >
    <component :is="currentPage" />
  </component>

</template>


<script>

  import { mapState } from 'vuex';
  import ImmersivePage from 'kolibri.coreVue.components.ImmersivePage';

  import { crossComponentTranslator } from 'kolibri.utils.i18n';
  import { PageNames } from '../constants';
  import SignInPage from './SignInPage';
  import SignUpPage from './SignUpPage';
  import ProfilePage from './ProfilePage';
  import ResetPasswordPage from './ResetPasswordPage';
  import SelectProfilePage from './SelectProfilePage';

  const translator = crossComponentTranslator(SignUpPage);

  const pageNameComponentMap = {
    [PageNames.SIGN_IN]: SignInPage,
    [PageNames.SIGN_UP]: SignUpPage,
    [PageNames.PROFILE]: ProfilePage,
    [PageNames.SELECT_PROFILE]: SelectProfilePage,
    [PageNames.RESET_PASSWORD]: ResetPasswordPage,
  };

  export default {
    name: 'UserIndex',
    components: {
      ImmersivePage,
    },
    computed: {
      ...mapState(['pageName']),
      /*
      appBarTitle() {
        if (this.pageName === PageNames.PROFILE) {
          return this.$tr('userProfileTitle');
        } else if (this.pageName === PageNames.SIGN_UP) {
          return translator.$tr('createAccount');
        } else if (this.pageName == PageNames.SELECT_PROFILE) {
          return 'Instant Schools';
        }
        return this.$tr('userSignInTitle');
      },
      */
      currentPage() {
        return pageNameComponentMap[this.pageName] || null;
      },
      PageNames() {
        return PageNames;
      },
    },
    $trs: {
      userProfileTitle: 'Account',
      userSignInTitle: 'Sign in',
      about: 'About',
    },
  };

</script>


<style lang="scss" scoped>
  /deep/ .ui-toolbar .link svg {
    fill: white!important;
  }
</style>
