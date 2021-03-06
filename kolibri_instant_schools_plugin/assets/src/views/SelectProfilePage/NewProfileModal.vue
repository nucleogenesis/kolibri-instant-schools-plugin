<template>
  <KModal
    :title="$tr('newProfileModalTitle')"
    @cancel="closeModal"
  >
    <div class="contents">
      <UiAlert
        v-if="showError"
        type="error"
        :dismissible="false"
      >
        {{ $tr('problemCreatingProfile') }}
      </UiAlert>

      <form @submit.prevent="submit">
        <KTextbox
          v-model="profileName"
          :autofocus="true"
          :label="$tr('profileName')"
          :invalid="!profileNameIsValid"
          :invalidText="profileNameInvalidText"
          :maxlength="120"
          :disabled="disabled"
          @blur="profileNameIsBlurred=true"
        />

        <div class="buttons">
          <KButton
            :text="$tr('cancel')"
            :primary="false"
            :disabled="disabled"
            @click="closeModal"
          />
          <KButton
            :text="$tr('save')"
            type="submit"
            :primary="true"
            :disabled="disabled"
          />
        </div>
      </form>
    </div>
  </KModal>
</template>

<script>

  import { mapState } from 'vuex';
  import KModal from 'kolibri.coreVue.components.KModal';
  import KTextbox from 'kolibri.coreVue.components.KTextbox';
  import KButton from 'kolibri.coreVue.components.KButton';
  import UiAlert from 'keen-ui/src/UiAlert';

  export default {
    name: 'NewProfileModal',
    components: {
      KModal,
      KButton,
      KTextbox,
      UiAlert,
    },
    props: {
      disabled: {
        type: Boolean,
        required: true,
      },
      showError: {
        type: Boolean,
        default: false,
      },
    },
    data() {
      return {
        formIsSubmitted: false,
        profileName: '',
        profileNameIsBlurred: false,
      };
    },
    computed: {
      ...mapState('signIn', ['profiles']),
      profileNameShouldValidate() {
        return this.profileName !== '' || this.profileNameIsBlurred || this.formIsSubmitted;
      },
      profileNameIsValid() {
        if (this.profileNameShouldValidate) {
          return this.profileName !== '' && !this.profileAlreadyExists(this.profileName);
        }
        return true;
      },
      profileNameInvalidText() {
        if (this.profileAlreadyExists(this.profileName)) {
          return this.$tr('profileAlreadyExists');
        }
        return this.$tr('required');
      },
    },
    methods: {
      profileAlreadyExists(profileName) {
        return Boolean(this.profiles.find(profile => profile.full_name === profileName));
      },
      submit() {
        this.formIsSubmitted = true;
        if (this.profileNameIsValid) {
          return this.$emit('submit', this.profileName);
        }
      },
      closeModal() {
        // Guard against closing during request until 'X' button can be removed from modal
        if (!this.disabled) {
          this.$emit('close');
        }
      },
    },
    $trs: {
      cancel: 'Cancel',
      profileName: 'Profile name',
      newProfileModalTitle: 'New profile',
      problemCreatingProfile: 'There was a problem creating this profile',
      profileAlreadyExists: 'This profile already exists',
      required: 'Required',
      save: 'Save',
    },
  };

</script>


<style lang="scss" scoped>

  .buttons {
    text-align: right;
  }

  button[type='submit'] {
    margin-right: 0;
  }

</style>
