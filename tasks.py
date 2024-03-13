from datetime import datetime  # noqa: I001
from crewai import Task


class AINewsLetterTasks():
    def fetch_news_task(self, agent):
        return Task(
            description=f'Fetch top AI news stories from the past 24 hours. The current time is {datetime.now()}.',  # noqa: E501
            agent=agent,
            async_execution=True,
            expected_output="""A list of top AI news story titles, URLs, and a brief summary for each story from the past 24 hours. 
                Example Output: 
                [
                    {  'title': 'China Unveils Economic Strategy to Boost AI Sector', 
                    'url': 'https://example.com/story1', 
                    'summary': 'AI made a splash in this year\'s Super Bowl commercials...'
                    }, 
                    {{...}}
                ]
            """  # noqa: E501
        )

    def analyze_news_task(self, agent, context):
        return Task(
            description='Analyze each news story and ensure there are at least 5 well-formatted articles. You must select the highlight news and set it as the title front matter and also generate a short subtitle front matter that captures the summary of the remaining newsletter stories. At last, generate the tags for the news letter and create the front matter for it.',  # noqa: E501
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A markdown-formatted analysis for each news story, including a rundown, detailed bullet points, 
                and a "Why it matters" section. There should be at least 5 articles, each following the proper format.
                Example Output: 
                '---\n
                Title: China Unveils Economic Strategy to Boost AI Sector\n
                Subtitle: India tightens AI regulation, concerns over AI in voting, and the impact on the metals market\n
                Tags: China, AI Strategy, Economic Policy, India, AI Regulation, Voting Technology, Metals Market, Global AI Trends\n\n
                ## China Unveils Economic Strategy to Boost AI Sector\n\n
                - **The Rundown:** China is set to reveal its strategy for supporting its slowing economy at the nation\'s most high-profile gathering. \n
                - **The details:**The future of the AI market in China is under discussion, with plans to outline its strategy to support its slowing economy.\n
                - **Why it matters:** China's economic strategies can shape the course of the global AI industry, making its growth significant to the global AI.[Read More](https://example.com/story1)\n\n           
            """  # noqa: E501
        )

    def compile_newsletter_task(self, agent, context, callback_function):
        return Task(
            description='Compile the newsletter with the frontm matter provided and Authors set to Marcel A. Lee, and the published date set to the current date',  # noqa: E501
            agent=agent,
            context=context,
            expected_output="""A complete newsletter in markdown format, with a consistent style and layout.
                Example Output: 
                `---\n
                Title: China Unveils Economic Strategy to Boost AI Sector\n
                Subtitle: India tightens AI regulation, concerns over AI in voting, and the impact on the metals market\n
                Tags: China, AI Strategy, Economic Policy, India, AI Regulation, Voting Technology, Metals Market, Global AI Trends\n
                Author: Marcel A. Lee\n
                Published Date: 2024-01-04\n
                ---\n\n
                ## China Unveils Economic Strategy to Boost AI Sector\n\n
                - **The Rundown:** China is set to reveal its strategy for supporting its slowing economy at the nation's most high-profile gathering.\n 
                - **The details:** The future of the AI market in China is under discussion, with plans to outline its strategy to support its slowing economy.\n
                - **Why it matters:** China's economic strategies can shape the course of the global AI industry, making its growth significant to the global AI market. [Read More](https://www.forexfactory.com/news/1270435-ai-market-outlook-for-march-4-2024)\n\n
                ## AI Impact on Metals Market\n\n
                - **The Rundown:** Breaking news about the world's most useful metals, curated from the top sources of global financial media.\n
                - **The details:** The impact of AI on the global metals market is under discussion.\n
                - **Why it matters:** The metals market is a significant part of the global economy, and AI's use in this sector can influence market trends and the broader financial landscape. [Read More](https://www.metalsmine.com/news/1270435-ai-market-outlook-for-march-4-2024)\n\n
                ## India Asks Tech Firms to Seek Approval Before Releasing Unreliable AI Tools\n\n
                - **The Rundown:** India has asked tech firms to seek its approval before the public release of AI tools that are considered unreliable.\n
                - **The details:** The Indian government is stepping up regulatory measures to ensure the quality and reliability of AI tools in the market.\n
                - **Why it matters:** Regulatory measures can shape the development and deployment of AI technologies, impacting their quality, reliability, and safety, which in turn affects businesses and consumers. [Read More](https://www.usnews.com/news/technology/articles/2024-03-04/india-asks-tech-firms-to-seek-approval-before-releasing-unreliable-ai-tools)\n\n
                ## AI Concerns Grow as Billions Prepare to Vote This Year\n\n
                - **The Rundown:** The influence of AI on the voting process is becoming a significant concern worldwide, especially as billions of people prepare for elections this year.\n
                - **The details:** Scholar and technology policy expert Alondra Nelson contributes to the discussion by highlighting the challenges AI poses to the voting process.\n
                - **Why it matters:** The potential influence of AI on democratic processes, particularly voting, underscores the importance of ensuring ethical and responsible use of AI. Insights from experts like Alondra Nelson can guide policy decisions to balance the benefits of AI with the need to safeguard democratic processes. [Read More](https://www.nhpr.org/2024-03-04/ai-concerns-grow-as-billions-of-people-worldwide-prepare-to-vote-this-year)\n\n
                `
            """, # noqa: E501
            callback=callback_function
        )
