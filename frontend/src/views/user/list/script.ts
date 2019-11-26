import Vue from 'vue';
import { mapActions, mapGetters } from 'vuex';
import { ModalConfig, ToastConfig } from 'buefy/types/components';
import { User, UserSearchOption } from '@/entity/user';
import { FETCH, HAS_ITEMS } from '@/store/constant';
import { SAVE_SUCCESS } from '@/views/constant';
import UserListItem from '@/views/user/list/item/UserListItem.vue';
import UserEdit from '@/views/user/edit/UserEdit.vue';


export default Vue.extend({
    data() {
        const option: UserSearchOption = {
            q: '',
        };

        return {
            option,
        };
    },
    components: {
        UserListItem,
    },
    mounted() {
        this.fetch(this.option);
    },
    computed: {
        ...mapGetters('user', [
            HAS_ITEMS,
        ]),
    },
    methods: {
        ...mapActions('user', [
            FETCH,
        ]),
        handleSearch(): void {
            this.fetch(this.option);
        },
        handleReset(): void {
            this.option.q = '';
        },
        handleNew(): void {
            this.openEditModal(new User());
        },
        openEditModal(user: User): void {
            const config: ModalConfig = {
                parent: this,
                component: UserEdit,
                hasModalCard: true,
                props: {
                    user,
                },
                events: {
                    [SAVE_SUCCESS]: () => {
                        const config: ToastConfig = {
                            message: '保存しました',
                            type: 'is-success',
                        };
                        this.$buefy.toast.open(config);
                        this.fetch(this.option);
                    },
                },
            };
            this.$buefy.modal.open(config);
        },
    },
});

