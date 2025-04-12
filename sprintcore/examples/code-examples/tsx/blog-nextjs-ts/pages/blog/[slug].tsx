import { GetStaticPaths, GetStaticProps } from 'next';
import { getAllPosts, getPostBySlug, Post } from '../../lib/posts';
import { remark } from 'remark';
import html from 'remark-html';

interface PostPageProps {
  post: Post & { contentHtml: string };
}

export const getStaticPaths: GetStaticPaths = async () => {
  const posts = getAllPosts();
  const paths = posts.map((post) => ({ params: { slug: post.slug } }));
  return { paths, fallback: false };
};

export const getStaticProps: GetStaticProps = async ({ params }) => {
  const slug = params?.slug as string;
  const post = getPostBySlug(slug);
  const processedContent = await remark().use(html).process(post.content);
  const contentHtml = processedContent.toString();

  return { props: { post: { ...post, contentHtml } } };
};

export default function PostPage({ post }: PostPageProps) {
  return (
    <div style={{ padding: '2rem' }}>
      
      <p><em>{post.date}</em></p>
      <div dangerouslySetInnerHTML={{ __html: post.contentHtml }} />
    </div>
  );
}
