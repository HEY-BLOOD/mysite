/* 文章正文 mdeditor编辑器控件的渲染 */
$(function () {
    editormd("id_body-wmd-wrapper", {
        watch: true, // 关闭实时预览
        lineNumbers: true,
        lineWrapping: false,
        width: "100% ",
        height: 500,
        placeholder: '',
        // 当有多个mdeditor时，全屏后，其他mdeditor仍然显示，解决此问题。
        onfullscreen : function() {
            this.editor.css("border-radius", 0).css("z-index", 9999);
        },
        onfullscreenExit : function() {
            this.editor.css({
                zIndex : 10,
                border : "1px solid rgb(221,221,221)"
            })
        },
        syncScrolling: "single",
        path: "/static/mdeditor/js/lib/",
        // theme
        theme : "default",
        previewTheme : "default",
        editorTheme : "default",

        saveHTMLToTextarea: true, // editor.md 有问题没有测试成功
        toolbarAutoFixed: true,
        searchReplace: true,
        emoji: true,
        tex: true,
        taskList: false,
        flowChart: true,
        sequenceDiagram: true,

        // image upload
        imageUpload: true,
        imageFormats: ['jpg', 'jpeg', 'gif', 'png', 'bmp', 'webp'],
        imageUploadURL: "/mdeditor/uploads/",
        toolbarIcons: function () {
            return ['undo', 'redo', '|', 'bold', 'del', 'italic', 'quote', '|', 'h1', 'h2', 'h3', 'h5', 'h6', '|', 'list-ul', 'list-ol', 'hr', '|', 'link', 'reference-link', 'image', 'code', 'preformatted-text', 'code-block', 'table', 'datetime', 'emoji', 'html-entities', 'pagebreak', 'goto-line', '|', 'help', 'info', '|', 'preview', 'watch', 'fullscreen']
        },
        onload: function () {
            console.log('onload', this);
            //this.fullscreen();
            //this.unwatch();
            //this.watch().fullscreen();

            //this.setMarkdown("#PHP");
            //this.width("100%");
            //this.height(480);
            //this.resize("100%", 640);
        }
    });

});
