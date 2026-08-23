import json

spec = {
  "spec_version": "1.0.0",
  "project": {
    "name": "test-demo",
    "version": "0.1.0",
    "framework": "Next.js",
    "framework_version": "13.3.1",
    "router_type": "Pages Router",
    "language": "TypeScript 5.0.4",
    "styling": "Tailwind CSS 3.3.1",
    "license": "MIT",
    "author": "Samuel_Ricardo"
  },
  "documentation_files": [
    {
      "filename": "README.md",
      "priority": "critical",
      "audiences": ["all"],
      "estimated_length": "150-200 lines",
      "required_sections": [
        "badges",
        "project_title_description",
        "tech_stack_table",
        "prerequisites",
        "quick_start_commands",
        "available_scripts",
        "project_structure_tree",
        "key_features_bullet_list",
        "testing_summary",
        "contributing_link",
        "license_reference"
      ],
      "optional_sections": ["deployment_notes", "faq"]
    },
    {
      "filename": "ARCHITECTURE.md",
      "priority": "high",
      "audiences": ["developers", "architects", "senior_engineers"],
      "estimated_length": "200-300 lines",
      "required_sections": [
        "architecture_overview",
        "system_context_diagram_mermaid",
        "container_diagram_mermaid",
        "component_diagram_mermaid",
        "data_flow_sequence_diagram_mermaid",
        "routing_architecture_description",
        "styling_architecture_tailwind_config",
        "state_management_rationale",
        "typescript_configuration",
        "build_configuration"
      ],
      "optional_sections": ["adr_links", "performance_notes", "scalability_considerations"]
    },
    {
      "filename": "TESTING.md",
      "priority": "high",
      "audiences": ["developers", "QA_engineers", "contributors"],
      "estimated_length": "150-250 lines",
      "required_sections": [
        "testing_philosophy_pyramid",
        "test_stack_details",
        "test_directory_structure_mirror",
        "running_test_commands_table",
        "coverage_thresholds_table",
        "unit_testing_patterns_rtl",
        "test_code_examples_real",
        "ci_integration_workflow"
      ],
      "optional_sections": ["integration_testing_approach", "e2e_testing_future", "debugging_tests_tips"]
    },
    {
      "filename": "CONTRIBUTING.md",
      "priority": "high",
      "audiences": ["contributors", "new_team_members"],
      "estimated_length": "200-300 lines",
      "required_sections": [
        "welcome_message",
        "code_of_conduct_summary",
        "getting_started_clone_setup",
        "development_workflow_branch_strategy",
        "coding_standards_eslint_ts",
        "testing_requirements_coverage_gate",
        "pull_request_process_checklist",
        "issue_reporting_templates"
      ],
      "optional_sections": ["release_process_semver", "contributor_recognition"]
    },
    {
      "filename": "API.md",
      "priority": "medium",
      "audiences": ["frontend_developers", "API_consumers"],
      "estimated_length": "100-150 lines",
      "required_sections": [
        "overview_base_url",
        "endpoints_table_hello",
        "request_response_examples_http",
        "error_handling_format",
        "status_codes_list"
      ],
      "optional_sections": ["rate_limiting", "versioning_strategy"]
    },
    {
      "filename": "DEPLOYMENT.md",
      "priority": "medium",
      "audiences": ["DevOps", "release_managers", "developers"],
      "estimated_length": "150-200 lines",
      "required_sections": [
        "deployment_overview_vercel_recommended",
        "vercel_setup_steps",
        "docker_deployment_option",
        "environment_variables_reference",
        "build_process_description",
        "performance_optimization_notes"
      ],
      "optional_sections": ["monitoring_observability", "security_headers"]
    },
    {
      "filename": "CHANGELOG.md",
      "priority": "medium",
      "audiences": ["all_stakeholders"],
      "estimated_length": "variable_per_release",
      "format": "Keep a Changelog 1.1.0",
      "required_sections_per_version": ["added", "changed", "deprecated", "removed", "fixed", "security"]
    },
    {
      "filename": "CODE_OF_CONDUCT.md",
      "priority": "low",
      "audiences": ["contributors", "community"],
      "format": "Contributor Covenant 2.1",
      "estimated_length": "100-150 lines"
    },
    {
      "filename": "SECURITY.md",
      "priority": "low",
      "audiences": ["security_researchers", "maintainers"],
      "estimated_length": "50-100 lines",
      "required_sections": ["supported_versions", "reporting_process", "disclosure_policy"]
    }
  ],
  "diagram_specifications": {
    "system_context_mermaid": {
      "diagram_type": "C4Context",
      "title": "System Context - test-demo",
      "mermaid_source_template": "C4Context\n    title System Context - test-demo\n    Person(user, \"User\", \"Accesses web app\")\n    System(testdemo, \"test-demo\", \"Next.js 13 Pages Router\", \"TypeScript, Tailwind, Jest\")\n    System_Ext(vercel, \"Vercel\", \"Hosting, CDN, Edge\")\n    System_Ext(github, \"GitHub\", \"Source control, CI\")\n    Rel(user, testdemo, \"Navigates / renders\", \"HTTPS\")\n    Rel(testdemo, vercel, \"Deploy / build\", \"Git push\")\n    Rel(github, vercel, \"Triggers deploy\", \"Webhook\")",
      "purpose": "Show external actors and system boundaries"
    },
    "container_mermaid": {
      "diagram_type": "C4Container",
      "title": "Container Diagram - test-demo",
      "containers": [
        {"id":"spa","label":"Next.js SPA","tech":"React 18, TypeScript"},
        {"id":"api","label":"API Routes","tech":"Next.js API Routes"},
        {"id":"cdn","label":"Vercel CDN","tech":"Edge Network, Static Assets"}
      ],
      "purpose": "Show internal containers within the system boundary"
    },
    "component_tree_mermaid": {
      "diagram_type": "flowchart TD",
      "title": "Component & Page Structure",
      "nodes": [
        {"id":"document","label":"_document.tsx","group":"layout"},
        {"id":"app","label":"_app.tsx","group":"layout"},
        {"id":"globals","label":"globals.css (Tailwind)","group":"styles"},
        {"id":"home","label":"pages/index.tsx (Home)","group":"pages"},
        {"id":"dashboard","label":"pages/dashboard/index.tsx","group":"pages"},
        {"id":"api_hello","label":"pages/api/hello.ts","group":"api"}
      ],
      "edges": [
        {"from":"document","to":"app"},
        {"from":"app","to":"globals"},
        {"from":"app","to":"home"},
        {"from":"app","to":"dashboard"},
        {"from":"app","to":"api_hello"}
      ],
      "purpose": "Show page component hierarchy and relationships"
    },
    "data_flow_mermaid": {
      "diagram_type": "sequenceDiagram",
      "title": "Data Flow - Page Render & API Call",
      "participants": [
        {"actor":"User"},
        {"actor":"Browser"},
        {"actor":"Next.js Server"},
        {"actor":"API Route"}
      ],
      "interactions": [
        {"actor":"User","target":"Browser","message":"Navigate to /dashboard"},
        {"actor":"Browser","target":"Next.js Server","message":"GET /dashboard"},
        {"actor":"Next.js Server","target":"Browser","message":"SSR HTML + JS bundle"},
        {"actor":"User","target":"Browser","message":"Clicks disabled button"},
        {"actor":"Browser","target":"API Route","message":"GET /api/hello"},
        {"actor":"API Route","target":"Browser","message":"JSON {name: John Doe}"}
      ],
      "purpose": "Show request lifecycle through server and API"
    },
    "test_coverage_mermaid": {
      "diagram_type": "pie",
      "title": "Target Coverage Thresholds",
      "values": [
        {"label":"Statements","percent":80},
        {"label":"Branches","percent":80},
        {"label":"Functions","percent":80},
        {"label":"Lines","percent":80}
      ],
      "purpose": "Show minimum CI gate thresholds"
    }
  },
  "code_examples_by_file": {
    "README.md": [
      {
        "section_ref": "quick_start_commands",
        "language": "bash",
        "snippet": "git clone <repository_url>\ncd test-demo\nnpm install\nnpm run dev\n# Open http://localhost:3000",
        "description": "Copy-paste quick start for new users"
      },
      {
        "section_ref": "test_commands",
        "language": "bash",
        "snippet": "npm run test        # Watch mode\nnpm run coverage    # With report",
        "description": "Common test execution commands"
      }
    ],
    "ARCHITECTURE.md": [
      {
        "section_ref": "typescript_config_example",
        "language": "json",
        "snippet": '{"compilerOptions":{"paths":{"@/*":["./src/*"],"@Pages/*":["./src/pages/*"]}}}',
        "description": "Actual tsconfig paths from codebase"
      },
      {
        "section_ref": "tailwind_config_example",
        "language": "javascript",
        "snippet": "module.exports = { content: ['./src/pages/**/*.{js,ts,jsx,tsx}'], theme: { extend: {} }, plugins: [] }",
        "description": "Tailwind config from tailwind.config.js"
      }
    ],
    "TESTING.md": [
      {
        "section_ref": "dashboard_tests_current",
        "language": "typescript",
        "snippet": "describe('Dashboard Page', () => { it('Should render properly', () => { render(<DashboardIndexPage/>); expect(screen.getByRole('heading')).toHaveTextContent('Hello World :D'); }); it('Should have disabled button', () => { render(<DashboardIndexPage/>); expect(screen.getByRole('button')).toBeDisabled(); }); it('P tag with blue class', () => { render(<DashboardIndexPage/>); const P = screen.getByTestId('paragraph-blue'); expect(P).toHaveClass('blue'); expect(P).toHaveTextContent('Pedro <:()'); }); });",
        "description": "Actual test from test/pages/index.test.tsx"
      },
      {
        "section_ref": "jest_config_example",
        "language": "javascript",
        "snippet": "const config = { testEnvironment: 'jest-environment-jsdom' }; export default createJestConfig(config);",
        "description": "Jest configuration from jest.config.mjs"
      },
      {
        "section_ref": "recommended_test_pattern",
        "language": "typescript",
        "snippet": "describe('Component', () => { it('renders with props', () => { render(<Component prop=\"value\" />); expect(screen.getByRole('element')).toBeInTheDocument(); }); });",
        "description": "Standard RTL test pattern for new components"
      }
    ],
    "API.md": [
      {
        "section_ref": "hello_endpoint_example",
        "language": "http",
        "snippet": "GET /api/hello HTTP/1.1\nHost: localhost:3000\nAccept: application/json\n\nHTTP/1.1 200 OK\nContent-Type: application/json\n\n{\"name\":\"John Doe\"}",
        "description": "Actual endpoint from src/pages/api/hello.ts"
      }
    ],
    "CONTRIBUTING.md": [
      {
        "section_ref": "conventional_commits_format",
        "language": "text",
        "snippet": "feat(scope): description\nfix(scope): description\ndocs: description\nrefactor: description\ntest: description",
        "description": "Conventional commit message format"
      },
      {
        "section_ref": "commit_message_examples",
        "language": "text",
        "snippet": "feat(dashboard): add profile widget\nfix(api): handle null response in hello endpoint\ndocs(readme): update quick start commands\nrefactor(components): extract reusable Button component\ntest(dashboard): add coverage for disabled button state",
        "description": "Realistic commit examples matching project"
      }
    ],
    "DEPLOYMENT.md": [
      {
        "section_ref": "env_example",
        "language": "env",
        "snippet": "NEXT_PUBLIC_APP_URL=http://localhost:3000\nNODE_ENV=production",
        "description": "Required environment variables"
      },
      {
        "section_ref": "dockerfile_sample",
        "language": "dockerfile",
        "snippet": "FROM node:18-alpine AS builder\nWORKDIR /app\nCOPY package*.json ./\nRUN npm ci\nCOPY . .\nRUN npm run build\nCMD [\"npm\", \"start\"]",
        "description": "Simplified Docker multi-stage build"
      }
    ]
  },
  "badge_specifications_readme": {
    "badge_row_template": "| Badge | Markdown | Description |",
    "badges": [
      {
        "name": "Build Status",
        "markdown": "[![Build Status](https://github.com/owner/repo/actions/workflows/ci.yml/badge.svg)](https://github.com/owner/repo/actions/workflows/ci.yml)",
        "description": "GitHub Actions CI workflow badge",
        "requires_action_config": True
      },
      {
        "name": "Coverage",
        "markdown": "[![Coverage](https://img.shields.io/codecov/c/github/owner/repo/main/test-demo)](https://codecov.io/gh/owner/repo)",
        "description": "Codecov test coverage percentage",
        "requires_action_config": True
      },
      {
        "name": "Version",
        "markdown": "[![Version](https://img.shields.io/github/package-json/v/owner/repo?filename=test-demo%2Fpackage.json)](https://github.com/owner/repo/blob/main/test-demo/package.json)",
        "description": "Current package version from package.json",
        "requires_action_config": False
      },
      {
        "name": "License MIT",
        "markdown": "[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)",
        "description": "MIT open source license",
        "requires_action_config": False
      },
      {
        "name": "Node.js",
        "markdown": "[![Node.js](https://img.shields.io/badge/node-%3E%3D18.0.0-brightgreen)](https://nodejs.org/)",
        "description": "Minimum required Node.js version",
        "requires_action_config": False
      },
      {
        "name": "Next.js",
        "markdown": "[![Next.js](https://img.shields.io/badge/Next.js-13.3.1-black?logo=next.js)](https://nextjs.org/)",
        "description": "Next.js framework version",
        "requires_action_config": False
      },
      {
        "name": "TypeScript",
        "markdown": "[![TypeScript](https://img.shields.io/badge/TypeScript-5.0.4-blue?logo=typescript)](https://www.typescriptlang.org/)",
        "description": "TypeScript compiler version",
        "requires_action_config": False
      },
      {
        "name": "Tailwind CSS",
        "markdown": "[![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3.3.1-38BDF8?logo=tailwind-css)](https://tailwindcss.com/)",
        "description": "Tailwind CSS utility framework version",
        "requires_action_config": False
      }
    ]
  },
  "section_templates_commonmark": {
    "heading_level_1": "# {title}",
    "heading_level_2": "## {title}",
    "heading_level_3": "### {title}",
    "heading_level_4": "#### {title}",
    "fenced_code_block": "```{language_identifier}\n{code_content}\n```",
    "inline_code_span": "`{code_snippet}`",
    "table_with_header": "| {col1_header} | {col2_header} |\n|---|---|\n| {row1_col1} | {row1_col2} |",
    "unordered_bullet": "- {item_text}",
    "ordered_numbered": "1. {item_text}",
    "task_pending": "- [ ] {task_description}",
    "task_completed": "- [x] {task_description}",
    "external_hyperlink": "[{link_text}]({url})",
    "internal_anchor_link": "[{text}]({#anchor_name})",
    "image_with_alt": "![{alternative_text}]({image_path} \"{optional_title}\")",
    "callout_note": "> **Note:** {note_content}",
    "callout_warning": "> **Warning:** {warning_content}",
    "callout_tip": "> **Tip:** {tip_content}",
    "callout_danger": "> **Danger:** {danger_content}",
    "callout_info": "> **Info:** {info_content}",
    "mermaid_diagram_block": "```mermaid\n{mermaid_diagram_code}\n```",
    "collapsible_details": "details>\nsummary>{summary_text}</summary>\n\n{expanded_content}\n\n</details>"
  },
  "commonmark_compliance_requirements": {
    "heading_style": "ATX-style (#, ##, ###) — never Setext (underline style)",
    "code_blocks": "Always fenced with language tag; never indented blocks",
    "lists": "Consistent marker (- for unordered; sequential numbers for ordered)",
    "escaping": "Escape <, >, & inside text nodes",
    "links": "Relative links preferred for internal navigation",
    "images": "Mandatory alt attribute for accessibility",
    "tables": "Header separator line required (|---|---|)",
    "raw_html": "Avoid raw HTML; prefer Markdown-native equivalents",
    "blank_lines": "Separate all block-level elements with blank lines",
    "line_length": "Soft limit ~100 characters; hard wrap at 120"
  },
  "post_generation_validation_checklist": [
    "Run markdownlint-cli2 against all .md files",
    "Verify Mermaid syntax renders correctly in preview",
    "Compile/test code examples against actual source",
    "Confirm all internal links point to existing sections",
    "Validate badge URLs respond with HTTP 200 or redirect",
    "Check CommonMark spec compliance (no non-standard syntax)",
    "Accessibility audit: heading hierarchy without skips, alt text present, contrast ratios adequate"
  ],
  "generation_order_for_technical_writer": [
    "1. README.md (start here — gives full context)",
    "2. ARCHITECTURE.md (understand structure before testing)",
    "3. TESTING.md (covers current tests in test/pages/index.test.tsx)",
    "4. CONTRIBUTING.md (establishes rules before others contribute)",
    "5. API.md (documents pages/api/hello.ts endpoint)",
    "6. DEPLOYMENT.md (production deployment instructions)",
    "7. CHANGELOG.md (version tracking from package.json v0.1.0)",
    "8. CODE_OF_CONDUCT.md (community standards)",
    "9. SECURITY.md (vulnerability disclosure process)"
  ]
}

with open('DOCUMENTATION_SPEC.json', 'w', encoding='utf-8') as f:
    json.dump(spec, f, indent=2, ensure_ascii=False)

print("DOCUMENTATION_SPEC.json written successfully.")
print(f"Total sections: {len(spec['documentation_files'])}")
print(f"Diagram specs: {len(spec['diagram_specifications'])}")
