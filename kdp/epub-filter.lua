-- Lua filter for EPUB generation: clean up front matter
--
-- Pandoc's --epub-title-page=true generates its own title page from metadata.
-- The LaTeX \titlepage also gets converted to a Div.titlepage in the AST.
-- This filter removes the LaTeX titlepage, adds an unlisted header to prevent
-- auto-generated front matter h1, and assigns CSS classes to front matter divs.

function Pandoc(doc)
  local new_blocks = {}
  local front_matter_index = 0
  local inserted_header = false

  for _, block in ipairs(doc.blocks) do
    -- Remove the LaTeX titlepage div (pandoc's auto title page handles this)
    if block.t == "Div" and block.classes:includes("titlepage") then
      -- skip it

    elseif front_matter_index < 2 and block.t == "Div" and block.classes:includes("center") then
      -- Before the first front matter div, insert an unlisted header
      if not inserted_header then
        local header = pandoc.Header(1, {},
          pandoc.Attr("front-matter", {"unnumbered", "unlisted"}))
        table.insert(new_blocks, header)
        inserted_header = true
      end

      -- Reclassify front matter center divs with proper CSS classes
      front_matter_index = front_matter_index + 1
      local class_map = {
        [1] = "copyright-page",
        [2] = "dedication-page"
      }
      block.classes = {class_map[front_matter_index]}
      table.insert(new_blocks, block)

    else
      front_matter_index = 2
      table.insert(new_blocks, block)
    end
  end

  doc.blocks = new_blocks
  return doc
end
