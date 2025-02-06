# 書体したい（`\textrm`）

```latex
% 欧文フォント
{\rmfamily ...} または \textrm{...}    % セリフ体・ローマン体（欧文デフォルト）
{\sffamily ...} または \textsf{...}    % サンセリフ体
{\ttfamily ...} または \texttt{...}    % タイプライタ体

% 和文フォント
{\mcfamily ...} または \textmc{...}    % 明朝体（和文デフォルト）
{\gtfamily ...} または \textgt{...}    % ゴシック体
{\mgfamily ...} または \textmg{...}    % 丸ゴシック体
```

本文中で局所的に書体（ファミリー）を切り替えることができます。
