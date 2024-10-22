<template>

  <CoreMenuOption
    icon="help"
    :label="$tr('about')"
    :link="url"
  >
    <mat-svg
      slot="icon"
      name="info_outline"
      category="action"
      :class="{ 'rtl-icon': isRtl }"
    />
  </CoreMenuOption>

</template>


<script>

  import { NavComponentSections } from 'kolibri.coreVue.vuex.constants';
  import CoreMenuOption from 'kolibri.coreVue.components.CoreMenuOption';
  import { crossComponentTranslator } from 'kolibri.utils.i18n';
  import registerNavItem from 'kolibri.utils.registerNavItem';
  import urls from 'kolibri.urls';

  const component = {
    name: 'AboutSideNavEntry',
    components: {
      CoreMenuOption,
    },
    $trs: {
      about: 'About',
    },
    priority: 10,
    url: urls['kolibri:kolibri_instant_schools_plugin:instant_schools_about'](),
    section: NavComponentSections.ACCOUNT,
    icon: 'info',
  };

  const translator = crossComponentTranslator(component);
  component.label = translator.$tr('about');

  registerNavItem(component);

  export default component;

</script>
