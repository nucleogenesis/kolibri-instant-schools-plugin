<template>

  <CoreMenuOption
    icon="login"
    :label="$tr('signIn')"
    :link="url"
  >
    <mat-svg
      slot="icon"
      name="exit_to_app"
      category="action"
      :class="{ 'rtl-icon': isRtl }"
    />
  </CoreMenuOption>

</template>


<script>

  import { UserKinds, NavComponentSections } from 'kolibri.coreVue.vuex.constants';
  import CoreMenuOption from 'kolibri.coreVue.components.CoreMenuOption';
  import { crossComponentTranslator } from 'kolibri.utils.i18n';
  import registerNavItem from 'kolibri.utils.registerNavItem';
  import routes from '../../routes';
  import urls from 'kolibri.urls';

  const component = {
    name: 'LoginSideNavEntry',
    components: {
      CoreMenuOption,
    },
    $trs: {
      signIn: 'Sign in',
    },
    url: urls['kolibri:kolibri_instant_schools_plugin:instant_schools_auth'](),
    role: UserKinds.ANONYMOUS,
    priority: 10,
    section: NavComponentSections.ACCOUNT,
    icon: 'login',
  };

  const translator = crossComponentTranslator(component);
  component.label = translator.$tr('signIn');

  registerNavItem(component);

  export default component;

</script>
