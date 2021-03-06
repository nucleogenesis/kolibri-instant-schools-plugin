<template>
  <KPageContainer>
    <KRouterLink
      ref="backButton"
      appearance="raised-button"
      :text="$tr('back')"
      :to="aboutRoute"
    />

    <iframe
      ref="iframe"
      width="100%"
      frameborder="0"
      :src="faqSrc"
      :height="height"
      @load="resizeIframe"
    >
    </iframe>

    <KButton
      :text="$tr('toTop')"
      :primary="true"
      :raised="true"
      class="to-top-button"
      :class="{ 'to-top-button-visible': btnIsVisible }"
      @click="goToTop"
    />
  </KPageContainer>
</template>


<script>

  import KPageContainer from 'kolibri.coreVue.components.KPageContainer';
  import KButton from 'kolibri.coreVue.components.KButton';
  import KRouterLink from 'kolibri.coreVue.components.KRouterLink';
  import throttle from 'lodash/throttle';
  import { PageNames } from '../../../constants';

  export default {
    name: 'FAQPage',
    $trs: {
      back: 'Back to about',
      toTop: 'Back to top',
    },
    components: {
      KButton,
      KPageContainer,
      KRouterLink,
    },
    data() {
      return {
        height: 5000,
        btnIsVisible: false,
      };
    },
    computed: {
      aboutRoute() {
        return { name: PageNames.ABOUT };
      },
      faqSrc() {
        return '/content/databases/about/faq.html';
      },
    },
    mounted() {
      this.resizeIframe();
      window.addEventListener('resize', this.throttleResizeIframe);
      document
        .querySelector('.content-container')
        .addEventListener('scroll', this.throttleUpdateBtnVisibility);
      // scroll to top
      document.querySelector('.content-container').scrollTop = 0;
    },
    beforeDestroy() {
      window.removeEventListener('resize', this.throttleResizeIframe);
      document
        .querySelector('.content-container')
        .removeEventListener('scroll', this.throttleUpdateBtnVisibility);
    },
    methods: {
      updateBtnVisibility() {
        this.btnIsVisible = document.querySelector('.content-container').scrollTop > 500;
      },
      throttleUpdateBtnVisibility: throttle(function() {
        this.updateBtnVisibility();
      }, 100),
      goToTop() {
        this.$refs.bacKButton.$el.scrollIntoView(false);
      },
      resizeIframe() {
        this.height = this.$refs.iframe.contentWindow.document.body.scrollHeight;
      },
      throttleResizeIframe: throttle(function() {
        this.resizeIframe();
      }, 100),
    },
  };

</script>


<style lang="scss" scoped>

  @import '~kolibri.styles.definitions';

  .faq-page {
    padding-bottom: 32px;
  }

  .to-top-button {
    position: fixed;
    right: 32px;
    bottom: 32px;
    display: none;
  }

  .to-top-button-visible {
    display: block;
  }

</style>
