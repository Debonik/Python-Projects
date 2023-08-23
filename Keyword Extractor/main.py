from textblob import TextBlob
import nltk
from collections import Counter

# Ensure NLTK corpora and punkt tokenizer models are downloaded
nltk.download('brown')
nltk.download('punkt')

def extract_keywords(text):
    if text and isinstance(text, str):
        blob = TextBlob(text)
        keywords = blob.noun_phrases

        # Count the frequency of each keyword
        keyword_counts = Counter(keywords)

        # Filter the keywords based on a threshold, e.g., only include keywords that appear more than once
        main_keywords = {keyword: count for keyword, count in keyword_counts.items() if count > 1}  # Adjust the threshold as needed

        return main_keywords
    else:
        raise ValueError("Input text must be a non-empty string.")

# Sample article (replace this with your 1000-word article)
article = """
In the digital age, the internet has become the backbone of
how we interact, work, learn, and entertain ourselves.
As our reliance on it grows, so does the importance of
the user experience on the websites we visit. One aspect that
has come to play a significant role in shaping this user
experience is Google’s Core Web Vitals. What Are Core Web Vitals?
Core Web Vitals is a set of metrics designed by Google to help website owners measure user experience on their sites. These vitals are made up of three main components: Largest Contentful Paint (LCP), First Input Delay (FID), and Cumulative Layout Shift (CLS). Each of these components plays a crucial role in how users perceive the performance of a website.

Diving Deeper Into Core Web Vitals
Largest Contentful Paint (LCP) is all about loading performance.
It measures how long it takes for the main content of a webpage to
load — that’s the largest image or text block visible within the user’s
view. Several factors can influence LCP, such as slow server response
times, render-blocking JavaScript and CSS, slow resource load times,
and client-side rendering.

First Input Delay (FID) measures interactivity.
This metric looks at the time it takes for a page
to become interactive — in other words, the delay
between when a user can first interact with a part
of the site (like clicking a link or button) and when
the interface responds. JavaScript execution can slow this down,
as can heavy resource load or long tasks.

Cumulative Layout Shift (CLS) assesses visual stability.
It quantifies the amount of unexpected shifting of web page
elements while the page is still downloading. Several factors
can lead to a high CLS, such as images without dimensions, ads,
embeds, and iframes without dimensions, dynamically injected content,
and web fonts causing FOIT/FOUT.

Importance Of Core Web Vitals
Core Web Vitals are essential for a few key reasons.

Firstly, they directly impact how users perceive your website. A site with good Core Web Vitals scores will be more enjoyable to use, leading to higher engagement and retention rates.

Secondly, Google has started using Core Web Vitals as ranking factors. This means that websites with better scores will be more likely to appear higher in search results.

Lastly, Core Web Vitals form a part of Google’s Page Experience Update, which is an algorithm update that takes various aspects of a user’s experience with a web page into account when determining search rankings.

What Are The Tools To Measure Core Web Vitals?
When it comes to measuring Core Web Vitals, there are several tools available that I have personally found to be extremely effective. These tools can help you identify areas of your website that might be affecting your performance and overall user experience.

Google PageSpeed Insights: This is a free tool offered by Google that provides information on how well a page performs on the Core Web Vitals metrics. Simply type in your webpage URL and it will give you a detailed report. This includes a performance score, detailed metrics about your webpage, and suggestions for improvement.

Chrome User Experience Report (CrUX): This tool from Google provides user experience metrics for how real-world Chrome users experience popular destinations on the web. It’s a big dataset, available for us to understand how real-world users experience our website.

Lighthouse: Another tool from Google, Lighthouse is an open-source, automated tool designed for improving the quality of web pages. It has audits for performance, accessibility, progressive web apps, SEO, and more. Lighthouse is available in Chrome DevTools, from the command line, and as a Node module. The Lighthouse report includes Core Web Vitals metrics that can be very useful in optimizing your website.

Web Vitals Chrome Extension: This extension provides instant access to the Core Web Vitals metrics data for any webpage. You just have to visit a page and you’ll see a small icon in your browser toolbar displaying the metrics.

Search Console: Google’s Search Console offers a Core Web Vitals report that helps you understand how your pages perform based on real-world usage data. It can also identify groups of pages that require attention.

WebPageTest: This is an advanced web performance tool that offers deep-dive information on a multitude of metrics, including Core Web Vitals. WebPageTest also offers filmstrip and video capture of the page load, which can help in visualizing content shifts.

These tools have their strengths, and using them together can give you a comprehensive understanding of your site’s Core Web Vitals. For instance, PageSpeed Insights and Lighthouse provide lab data that can be helpful for debugging performance issues, while CrUX and Search Console provide field data that reflects real-world user experiences. By utilizing these tools, you can ensure that your web pages are well-optimized and provide a good user experience, which is critical in today’s web environment.

How To Improve Your Core Web Vitals Scores?
Improving your Core Web Vitals scores primarily involves addressing the issues that affect LCP, FID, and CLS.

To optimize LCP, consider actions like removing any unnecessary third-party scripts, upgrading your web host, setting up lazy loading for images, and removing large page elements.

Improving FID involves optimizing how browsers parse and execute your JavaScript. Break up Long Tasks, optimize your page for interaction readiness, and use a web worker.

For a better CLS score, always include size attributes on your images and video elements, ensure ads elements have a reserved space, and avoid inserting content above existing content.

How To Improve Cumulative Layout Shift (CLS)?
CLS is a measure of visual stability on your website. It calculates how much visible elements shift unexpectedly during page load. A high CLS can cause a poor user experience, as page elements can move around and cause accidental clicks. Therefore, achieving a low CLS score should be a priority for enhancing user experience and Core Web Vitals.

Include Size Attributes on Images and Video Elements
Including width and height size attributes on your images and videos is crucial in preventing layout shifts. When the browser loads your webpage, it can allocate the correct amount of space for these elements even before they load, ensuring the rest of your content doesn’t move around unexpectedly.

If you’re using CSS to style your images and videos, ensure that the CSS sizes match the actual image sizes. Alternatively, you can use CSS aspect ratio boxes to reserve the right space for any element, which is especially handy for responsive design.

Ensure Ads Elements Have a Reserved Space
Ads are a common cause of bad CLS scores, as they often load separately from the main content and can push content down the page. To prevent this, always allocate a static space for ads. This can be done using a placeholder or fallback that is the same size as the ad unit.

Avoid Inserting Content Above Existing Content
Inserting new content above existing content, especially after the page starts loading, pushes down content and creates a layout shift. This can be avoided by designing your site to have new content added below the fold or at the end of the article, or by using overlays or expandable sections that don’t shift the rest of the page content.

Use Web Fonts Effectively
Web fonts can also cause layout shifts if not appropriately handled. The browser may lay out text using a fallback font and then re-layout the page once the web font loads, causing a shift. To prevent this, you can preload key web fonts, use font display options to control how and when web fonts load, or use modern formats like variable fonts that are more efficient.

Animation Transitions
If you have elements on your page that change position, make sure to use animations or transitions to smoothly guide the user’s attention rather than causing an abrupt layout shift.

Remember, the goal is to create a stable, enjoyable user experience. Ensuring elements on your page don’t shift unexpectedly is a crucial part of this, and the effort you put into optimizing your CLS score will go a long way toward improving your overall Core Web Vitals.

How To Improve Largest Contentful Paint (LCP)?
LCP measures loading performance. It’s the time it takes for the largest image or text block in the user’s viewport to become fully rendered. To provide a good user experience, LCP should occur within 2.5 seconds of when the page first starts loading. Here’s how you can improve LCP:

Optimize Your Server Response Times
Your server response time can significantly impact LCP. Implementing a Content Delivery Network (CDN), optimizing your server, and improving your server’s backend logic can all help reduce your server response time.

Remove Render-Blocking JavaScript and CSS
Render-blocking JavaScript and CSS can prevent a page from loading quickly. To optimize, you can minify your CSS and JavaScript files, defer non-critical CSS and JavaScript, and inline critical CSS.

Optimize and Compress Images
Large images take longer to load, which can delay LCP. Optimizing and compressing your images, using modern, efficient formats like WebP, and leveraging lazy loading where appropriate can help improve LCP.

Preload Important Resources
Preloading can inform the browser in advance about important resources that will be needed soon. By adding a rel=”preload” attribute to key resources, you can speed up their delivery and improve LCP.

Improve Client-Side Rendering
Client-side rendering can be a bottleneck for LCP, especially for JavaScript-heavy applications. Techniques such as server-side rendering (SSR), pre-rendering, or using a JavaScript framework optimized for faster rendering can improve LCP.

Use a Fast, Reliable Hosting Service
The speed of your web host can directly impact LCP. Choose a hosting provider that offers sufficient resources, high uptime, and fast response times.

Implement Dynamic Content Caching
Caching allows a browser to store a version of your website’s resources locally, significantly speeding up subsequent loads. Dynamic content, such as HTML documents, can also be cached to improve LCP.

Optimize the Critical Rendering Path
The Critical Rendering Path is the sequence of tasks the browser performs to render the initial view of a webpage. Optimizing this path involves minimizing the number of critical resources: they can be reduced, prioritized, or loaded asynchronously.

Avoid adding large elements to your webpage
Large page elements can slow down LCP. If possible, try to minimize the size of the largest elements on your page.

By focusing on these areas, you can significantly improve your website’s LCP times, leading to a better user experience and potentially higher rankings in search engine results.

How To Improve First Input Delay (FID)?
FID measures the time from when a user first interacts with your page (like clicking a link or a button) to the time the browser is actually able to respond to that interaction. A good FID score is less than 100 milliseconds. Here are some strategies to improve FID:

Minimize (or defer) JavaScript
It’s almost impossible to avoid JavaScript entirely when building modern web applications, but excessive JavaScript execution times can significantly impact FID. To minimize its impact, only send the code your users need and defer non-critical JavaScript until after the first paint.

Remove Any Non-Critical Third-Party Scripts
Third-party scripts, especially if they’re not critical, can negatively impact FID. This includes scripts for advertising, analytics, and social media embeds, among others. Consider delaying the loading of these scripts until after the main content of your page has loaded.

Use a Web Worker
Web Workers allow you to run JavaScript on a background thread, separate from the main execution thread of a web page. This means the main thread is free to stay responsive to user input, thereby improving FID.

Break Up Long Tasks
Long tasks are JavaScript tasks that block the main thread for 50 milliseconds or more. Break up long tasks into smaller, asynchronous tasks to keep the main thread available and improve FID.

Optimize Your Page for Interaction Readiness
This means making sure that the different parts of your page are interactive as soon as they’re displayed. You can achieve this by prioritizing the loading and execution of the parts of JavaScript needed for interaction.

Use Passive Event Listeners
Passive event listeners are a way to tell the browser that you won’t prevent a scroll event, meaning it can continue to render and respond to user interactions. This can help improve FID.

By focusing on these strategies, you can ensure a smoother, more responsive experience for your users, leading to better engagement and satisfaction. Remember, a good FID score is a critical part of providing a great user experience and can even influence your site’s visibility in search engine results.

Preparing For The Future Of Core Web Vitals
Core Web Vitals are not set in stone. Google has indicated that they will continue to evolve as user expectations of what makes a good web experience change, and as new technologies and capabilities emerge on the web.

Staying ahead of the curve will involve regular monitoring and optimization of your site’s performance. This means making use of the tools available to you, like Google Search Console, Lighthouse, and PageSpeed Insights, to regularly check on your Core Web Vitals scores and identify any areas for improvement.

But it’s not just about reacting to changes in the metrics. A forward-thinking approach also involves keeping an eye on emerging technologies and web standards that could help you improve site performance. This includes understanding and implementing modern image formats, like WebP and AVIF, using resource hints like preload and prefetch to help the browser make better decisions about resource prioritization, and leveraging new CSS features like content-visibility and contain-intrinsic-size that can help improve rendering performance.

Conclusion
Core Web Vitals have firmly established themselves as a crucial aspect of the modern web. They provide objective, measurable ways to assess a user’s experience on a webpage, and they offer actionable insights for improvements. But perhaps most importantly, they encourage a shift in perspective — from focusing solely on what we want to show users, to considering what users want to see and how they want to interact with our sites.

Understanding and optimizing for Core Web Vitals is not a luxury, but a necessity for any website owner who wants to offer a top-tier user experience and rank well in search engine results. By taking a proactive approach to these metrics, you’ll create a better web experience for your users and set your website up for continued success in the ever-changing landscape of the internet.

"""

if len(article.split()) < 1000:
    print("Warning: The article is less than 1000 words. Please provide a longer article for more accurate analysis.")

try:
    keywords_with_frequency = extract_keywords(article)
    print("Main Keywords with Frequency:")
    for keyword, frequency in keywords_with_frequency.items():
        print(f"Keyword: {keyword} - Frequency: {frequency}")
except Exception as e:
    print("An error occurred:", str(e))