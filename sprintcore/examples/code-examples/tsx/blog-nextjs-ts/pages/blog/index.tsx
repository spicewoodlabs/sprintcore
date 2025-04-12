import Link from 'next/link';
import { GetStaticProps } from 'next';
import { getAllPosts, PostMeta } from '../../lib/posts';

interface BlogProps {
  posts: PostMeta[];
}

export const getStaticProps: GetStaticProps = async () => {
  const posts = getAllPosts();
  return { props: { posts } };
};

export default function Blog({ posts }: BlogProps) {
  return (
    <div style={{ padding: '2rem' }}>
      <h1>📝 Blog</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.slug}>
            <Link href={`/blog/${post.slug}`}>
              {post.title} — <em>{post.date}</em>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
