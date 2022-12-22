import method_decorator as method_decorator
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import OgiriPost, OgiriPostForm, ReverseOgiriPostForm, ImageOgiriPostForm, ImitationOgiriPostForm
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator

class IndexView(TemplateView):

    template_name = 'index.html'

class AnswerCategory(TemplateView):

    template_name = 'answer_list.html'


class ThemaCategory(TemplateView):

    template_name = 'thema_list.html'



# デコレーターにより、CreateOgiriViewへのアクセスはログインユーザーに限定される
# ログイン状態でなければsetting.pyのLOGIN_URLにリダイレクトされる
@method_decorator(login_required, name='dispatch')
class CreateOgiriView(CreateView):
    '''写真投稿のページのビュー

    OgiriPostFormで定義されているモデルとフィールドと連携して
    投稿データをデータベースに登録する

    Attributes:
        form_class: モデルとフィールドが登録されたフォームクラス
        template_name: レンダリングするテンプレート
        success_url: データベースへの登録完了後のリダイレクト先
    '''
    # forms.pyのBookPostFormをフォームクラスとして登録
    form_class = OgiriPostForm

    # レンダリングするテンプレート
    template_name = "thema_post.html"
    # フォームデータ完了後のリダイレクト先
    success_url = reverse_lazy('Ogiri:post_done')

    def get_initial(self):
        initial = super().get_initial()
        initial["category"] = 1
        return initial

    def form_valid(self, form):
        '''CreateViewクラスのform_valid()をオーバーライド

        フォームのバリデーションを通過したときに呼ばれる
        フォームのデータ登録をここで行う

        :param form:
        :return:
        '''

        # commit=FalseにしてPostされたデータを取得
        postdata = form.save(commit=False)
        #　投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CreateReverseOgiriView(CreateView):

    form_class = ReverseOgiriPostForm

    # レンダリングするテンプレート
    template_name = "reverse_thema_post.html"
    # フォームデータ完了後のリダイレクト先
    success_url = reverse_lazy('Ogiri:post_done')

    def get_initial(self):
        initial = super().get_initial()
        initial["category"] = 2
        return initial

    def form_valid(self, form):


        # commit=FalseにしてPostされたデータを取得
        postdata = form.save(commit=False)
        #　投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CreateImageOgiriView(CreateView):

    form_class = ImageOgiriPostForm

    # レンダリングするテンプレート
    template_name = "image_thema_post.html"
    # フォームデータ完了後のリダイレクト先
    success_url = reverse_lazy('Ogiri:post_done')

    def get_initial(self):
        initial = super().get_initial()
        initial["category"] = 4
        return initial

    def form_valid(self, form):


        # commit=FalseにしてPostされたデータを取得
        postdata = form.save(commit=False)
        #　投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class CreateImitationOgiriView(CreateView):

    form_class = ImitationOgiriPostForm

    # レンダリングするテンプレート
    template_name = "imitation_thema_post.html"
    # フォームデータ完了後のリダイレクト先
    success_url = reverse_lazy('Ogiri:post_done')

    def get_initial(self):
        initial = super().get_initial()
        initial["category"] = 3
        return initial

    def form_valid(self, form):


        # commit=FalseにしてPostされたデータを取得
        postdata = form.save(commit=False)
        #　投稿ユーザーのidを取得してモデルのuserフィールドに格納
        postdata.user = self.request.user
        # 投稿データをデータベースに登録
        postdata.save()
        # 戻り値はスーパークラスのform_valid()の戻り値(HttpResponseRedirect)
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    '''投稿完了ページのビュー

    '''
    template_name = 'post_complete.html'

