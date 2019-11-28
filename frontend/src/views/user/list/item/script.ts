import Vue from 'vue';
import { mapActions } from 'vuex';
import { DialogConfig, ToastConfig } from 'buefy/types/components';
import { User } from '@/entity/user';
import { DELETE } from '@/store/constant';
import { OPEN_EDIT_MODAL } from '@/views/constant';


export default Vue.extend({
    template: '<user-list-item/>',
    props: {
        user: {
            required: true,
            type: User,
        },
    },
    methods: {
        ...mapActions('user', [
            DELETE,
        ]),
        handleEdit(): void {
            // 親componentのイベント使う
            this.$emit(OPEN_EDIT_MODAL, this.user);
        },
        handleDelete(): void {
            const message: string = `
                <p>${this.user.name}を削除しますか？</p>
                <small>注: 削除したユーザーは元に戻すことができません。</small>
            `;
            const config: DialogConfig = {
                title: 'ユーザー削除',
                message,
                confirmText: '削除',
                cancelText: '閉じる',
                hasIcon: true,
                type: 'is-danger',
                onConfirm: () => {
                    this._doDelete();
                },
            };

            this.$buefy.dialog.confirm(config);
        },
        _doDelete(): void {
            this.delete(this.user.id)
                .then(() => {
                    const config: ToastConfig = {
                        message: '削除しました',
                        type: 'is-success',
                    };
                    this.$buefy.toast.open(config);
                    this.$emit('');
                });
        },
    },
});

